import asyncio
import random
from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from states.quiz_states import QuizState
from questions import QUESTIONS
from database.crud import get_or_create_user, decrease_user_attempts, update_user_best_score
from keyboards.inline import make_quiz_keyboard
from keyboards.reply import main_menu_keyboard # <-- Импортируем нашу главную клавиатуру

router = Router()

# 1. --- Новая функция для таймера ---
async def timer_expired(message: Message, state: FSMContext, session: AsyncSession):
    """
    Эта функция вызывается, если пользователь не ответил за 10 секунд.
    """
    await asyncio.sleep(10)

    current_state = await state.get_state()
    if current_state != QuizState.in_game:
        return

    data = await state.get_data()
    score = data.get("score", 0)
    user_id = data.get("user_id")

    # --- Возвращаем клавиатуру меню после истечения времени ---
    await message.answer(f"⏰ <b>Время вышло!</b>\n\nИгра окончена. Ваш счет: <b>{score}</b>", reply_markup=main_menu_keyboard())
    
    await update_user_best_score(session, user_id, score)
    await state.clear()


# --- Вспомогательная функция для отправки вопроса (модифицирована) ---
async def send_question(message: Message, state: FSMContext, session: AsyncSession):
    data = await state.get_data()
    questions_list = data.get("questions")
    
    if not questions_list:
        score = data.get("score", 0)
        await message.answer(f"🎉 <b>Поздравляем!</b> 🎉\n\nВы ответили на все вопросы!\nВаш счет: <b>{score}</b>")
        await state.clear()
        return

    current_question = questions_list[0]
    keyboard = make_quiz_keyboard(current_question["options"])
    
    sent_message = await message.answer(f"<b>Вопрос:</b> {current_question['text']}", reply_markup=keyboard)
    
    # 2. --- Запускаем таймер в фоновом режиме ---
    # Создаем фоновую задачу, которая завершит игру через 10 секунд
    timer_task = asyncio.create_task(
        timer_expired(sent_message, state, session)
    )
    # Сохраняем задачу в FSM, чтобы мы могли ее отменить при получении ответа
    await state.update_data(timer_task=timer_task)


# --- Хэндлер для кнопки "Начать игру 🚀" (модифицирован) ---
@router.message(F.text == "Начать игру 🚀")
async def start_quiz(message: Message, session: AsyncSession, state: FSMContext):
    user, _ = await get_or_create_user(session, message.from_user.id, message.from_user.full_name, message.from_user.username)

    if user.attempts_left <= 0:
        await message.answer("У вас закончились попытки на сегодня. Возвращайтесь завтра!")
        return
    
    await decrease_user_attempts(session, user.user_id)
    
    shuffled_questions = random.sample(QUESTIONS, len(QUESTIONS))
    
    await state.set_state(QuizState.in_game)
    await state.update_data(
        questions=shuffled_questions,
        score=0,
        user_id=user.user_id,
        timer_task=None
    )
    
    # --- ИЗМЕНЕНИЕ ЗДЕСЬ ---
    # Отправляем сообщение со специальным объектом ReplyKeyboardRemove(),
    # который и дает Telegram команду убрать клавиатуру меню.
    await message.answer(
        "Игра начинается! У вас есть <b>10 секунд</b> на ответ на каждый вопрос.",
        reply_markup=ReplyKeyboardRemove()
    )
    
    await send_question(message, state, session)


# --- Хэндлер для ответов на вопросы (модифицирован) ---
@router.callback_query(QuizState.in_game, F.data.startswith("answer:"))
async def handle_answer(call: CallbackQuery, session: AsyncSession, state: FSMContext):
    data = await state.get_data()
    
    timer_task = data.get("timer_task")
    if timer_task:
        timer_task.cancel()

    user_answer = call.data.split(":")[1]
    
    questions_list = data.get("questions")
    current_question = questions_list[0]
    correct_answer = current_question["correct_answer"]
    
    await call.message.edit_reply_markup(reply_markup=None)

    if user_answer == correct_answer:
        score = data.get("score", 0) + 1
        remaining_questions = questions_list[1:]
        await state.update_data(score=score, questions=remaining_questions)

        await call.message.answer(f"✅ Правильно!\n\nВаш счет: <b>{score}</b>")

        if not remaining_questions:
            # --- Возвращаем клавиатуру меню после последнего вопроса ---
            await call.message.answer(f"🎉 <b>Квиз завершен!</b> 🎉\n\nВаш итоговый счет: <b>{score}</b>", reply_markup=main_menu_keyboard())
            await update_user_best_score(session, data.get("user_id"), score)
            await state.clear()
        else:
            await send_question(call.message, state, session)
    else:
        score = data.get("score", 0)
        # --- Возвращаем клавиатуру меню после неправильного ответа ---
        await call.message.answer(
            f"❌ <b>Неверно!</b>\n\nПравильный ответ: <b>{correct_answer}</b>\n\n"
            f"Игра окончена. Ваш счет: <b>{score}</b>",
            reply_markup=main_menu_keyboard() # <-- ВОЗВРАЩАЕМ КЛАВИАТУРУ
        )
        await update_user_best_score(session, data.get("user_id"), score)
        await state.clear()
        
    await call.answer()