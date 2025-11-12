import asyncio
import random
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from states.quiz_states import QuizState
from questions import QUESTIONS
from database.crud import get_or_create_user, decrease_user_attempts, update_user_best_score
from keyboards.inline import make_quiz_keyboard
from keyboards.reply import main_menu_keyboard


router = Router()


# --- Таймер (10 секунд) ---
async def timer_expired(message: Message, state: FSMContext, session: AsyncSession):
    await asyncio.sleep(10)

    current_state = await state.get_state()
    if current_state != QuizState.in_game:
        return

    data = await state.get_data()
    score = data.get("score", 0)
    user_id = data.get("user_id")

    await message.answer(
        f"⏰ <b>Время вышло!</b>\n\nИгра окончена. Ваш счёт: <b>{score}</b>",
        reply_markup=main_menu_keyboard()
    )
    await update_user_best_score(session, user_id, score)
    await state.clear()


# --- Отправка одного случайного вопроса (бесконечно) ---
async def send_question(message: Message, state: FSMContext, session: AsyncSession):
    # 🔁 Случайный вопрос из полного списка — повторы возможны!
    current_question = random.choice(QUESTIONS)

    keyboard = make_quiz_keyboard(current_question["options"])
    sent_message = await message.answer(
        f"<b>Вопрос:</b> {current_question['text']}",
        reply_markup=keyboard
    )

    # Сохраняем текущий вопрос для проверки ответа
    await state.update_data(current_question=current_question)

    # Запускаем таймер
    timer_task = asyncio.create_task(timer_expired(sent_message, state, session))
    await state.update_data(timer_task=timer_task)


# --- Начало игры ---
@router.message(F.text == "Начать игру 🚀")
async def start_quiz(message: Message, session: AsyncSession, state: FSMContext):
    user, _ = await get_or_create_user(
        session,
        message.from_user.id,
        message.from_user.full_name,
        message.from_user.username
    )

    if user.attempts_left <= 0:
        await message.answer(
            "У вас закончились попытки на сегодня. Возвращайтесь завтра!\n\n"
            "💡 <b>Совет:</b> Пригласите друга — получите дополнительные попытки!"
        )
        return

    await decrease_user_attempts(session, user.user_id)

    # Инициализация состояния: только счёт и user_id
    await state.set_state(QuizState.in_game)
    await state.update_data(
        score=0,
        user_id=user.user_id
    )

    await message.answer(
        "Игра начинается! У вас есть <b>10 секунд</b> на ответ на каждый вопрос.",
        reply_markup=ReplyKeyboardRemove()
    )
    
    # Первый случайный вопрос
    await send_question(message, state, session)


# --- Обработка ответа ---
@router.callback_query(QuizState.in_game, F.data.startswith("answer:"))
async def handle_answer(call: CallbackQuery, session: AsyncSession, state: FSMContext):
    data = await state.get_data()

    # Отменяем таймер
    timer_task = data.get("timer_task")
    if timer_task and not timer_task.done():
        timer_task.cancel()

    # Извлекаем данные
    user_answer = call.data.replace("answer:", "", 1)
    current_question = data.get("current_question")

    if not current_question:
        await call.message.answer("Ошибка данных. Попробуйте начать игру заново.")
        await state.clear()
        await call.answer()
        return

    correct_answer = current_question["correct_answer"]
    score = data.get("score", 0)

    await call.message.edit_reply_markup(reply_markup=None)

    if user_answer == correct_answer:
        # ✅ Правильно → +1 очко → следующий случайный вопрос (бесконечно!)
        score += 1
        await state.update_data(score=score)
        await call.message.answer(f"✅ Правильно!\nВаш счёт: <b>{score}</b>")
        await send_question(call.message, state, session)
    else:
        # ❌ Неверно → завершить игру
        await call.message.answer(
            f"❌ <b>Неверно!</b>\n\nПравильный ответ: <b>{correct_answer}</b>\n\n"
            f"Игра окончена. Ваш счёт: <b>{score}</b>",
            reply_markup=main_menu_keyboard()
        )
        await update_user_best_score(session, data["user_id"], score)
        await state.clear()

    await call.answer()