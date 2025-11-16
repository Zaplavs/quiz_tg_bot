import asyncio
import html
from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.fsm.context import FSMContext

from filters.admin import IsAdmin
from states.admin_states import BroadcastState
from keyboards.inline import ( # <-- Обновляем импорт клавиатур
    admin_main_keyboard,
    admin_stats_keyboard,
    broadcast_confirm_keyboard
)
# --- ИЗМЕНЕНИЕ ЗДЕСЬ ---
from database import admin_crud as crud

router = Router()

# Этот хэндлер срабатывает на команду /admin и только для админа (благодаря фильтру IsAdmin)
@router.message(Command("admin"), IsAdmin())
async def cmd_admin(message: Message):
    await message.answer("Добро пожаловать в админ-панель!", reply_markup=admin_main_keyboard())


# Этот хэндлер используется для кнопки "Назад", чтобы вернуться в главное меню админки
@router.callback_query(F.data == "admin:main", IsAdmin())
async def back_to_main_admin_menu(call: CallbackQuery):
    # Используем edit_text, чтобы изменить существующее сообщение, а не отправлять новое
    await call.message.edit_text("Добро пожаловать в админ-панель!", reply_markup=admin_main_keyboard())
    # Отвечаем на callback, чтобы у пользователя пропали "часики" на кнопке
    await call.answer()


# --- Раздел "Статистика и Информация" ---

# Этот хэндлер открывает подменю статистики
@router.callback_query(F.data == "admin:stats", IsAdmin())
async def admin_stats_menu(call: CallbackQuery):
    await call.message.edit_text("Раздел: Статистика и Информация", reply_markup=admin_stats_keyboard())
    await call.answer()


# Этот хэндлер собирает и показывает общую статистику
@router.callback_query(F.data == "admin:general_stats", IsAdmin())
async def get_general_stats(call: CallbackQuery, session: AsyncSession):
    # Отправляем моментальный ответ, чтобы пользователь видел, что запрос обрабатывается
    await call.answer("Собираю статистику...")
    
    # Используем asyncio.gather для параллельного выполнения всех запросов к БД.
    # Это намного быстрее, чем делать их по одному.
    total, today, week, active_today = await asyncio.gather(
        crud.count_users(session),
        crud.count_new_users_for_period(session, days=1),
        crud.count_new_users_for_period(session, days=7),
        crud.count_active_users_today(session)
    )

    # Формируем красивое сообщение со статистикой
    stats_text = (
        f"<b>📈 Общая статистика бота:</b>\n\n"
        f"👤 Всего пользователей: <b>{total}</b>\n"
        f"☀️ Новых за сегодня: <b>{today}</b>\n"
        f"📅 Новых за неделю: <b>{week}</b>\n"
        f"🎮 Активных игроков сегодня: <b>{active_today}</b>"
    )
    await call.message.edit_text(stats_text, reply_markup=admin_stats_keyboard())


# Этот хэндлер показывает список победителей за текущую неделю
@router.callback_query(F.data == "admin:weekly_winners", IsAdmin())
async def get_weekly_winners_list(call: CallbackQuery, session: AsyncSession):
    await call.answer("Загружаю список...")
    winners = await crud.get_weekly_winners(session)

    # Обрабатываем случай, когда победителей еще нет
    if not winners:
        await call.message.edit_text(
            "На этой неделе еще не было победителей.",
            reply_markup=admin_stats_keyboard()
        )
        return
    
    # Формируем список победителей
    winners_list = "<b>🏆 Список победителей недели:</b>\n\n"
    for winner in winners:
        # Используем html.escape для безопасности, чтобы имя пользователя не сломало HTML-разметку
        user_name = html.escape(winner.full_name)
        winners_list += f"• {user_name} (@{winner.username or 'N/A'}, ID: <code>{winner.user_id}</code>)\n"
    
    await call.message.edit_text(winners_list, reply_markup=admin_stats_keyboard())


@router.callback_query(F.data == "admin:broadcast_start", IsAdmin())
async def start_broadcast(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Пришлите сообщение, которое вы хотите разослать всем пользователям.")
    # Устанавливаем состояние ожидания сообщения
    await state.set_state(BroadcastState.waiting_for_message)
    await call.answer()

# 2. Получение сообщения для рассылки и запрос подтверждения
@router.message(BroadcastState.waiting_for_message, IsAdmin())
async def get_broadcast_message(message: Message, state: FSMContext):
    # Показываем админу предпросмотр
    await message.copy_to(chat_id=message.from_user.id)
    await message.answer(
        "Вы уверены, что хотите отправить это сообщение всем пользователям?",
        reply_markup=broadcast_confirm_keyboard()
    )
    # Сохраняем ID сообщения, которое нужно будет разослать
    await state.update_data(broadcast_message_id=message.message_id)
    await state.set_state(BroadcastState.waiting_for_confirmation)

# 3. Подтверждение и запуск рассылки
@router.callback_query(F.data == "admin:broadcast_confirm", BroadcastState.waiting_for_confirmation, IsAdmin())
async def confirm_broadcast(call: CallbackQuery, state: FSMContext, session: AsyncSession, bot: Bot):
    data = await state.get_data()
    broadcast_message_id = data.get('broadcast_message_id')
    
    # Сбрасываем состояние, чтобы админ мог пользоваться другими командами
    await state.clear()
    
    await call.message.edit_text("✅ Рассылка запущена! Это может занять некоторое время.")
    await call.answer()

    # Запускаем саму рассылку в фоновом режиме
    asyncio.create_task(
        start_mailing(session, bot, call.from_user.id, broadcast_message_id)
    )

# 4. Отмена рассылки
@router.callback_query(F.data == "admin:broadcast_cancel", BroadcastState.waiting_for_confirmation, IsAdmin())
async def cancel_broadcast(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.edit_text("Рассылка отменена.", reply_markup=None)
    # Возвращаем в главное меню админки
    await call.message.answer("Добро пожаловать в админ-панель!", reply_markup=admin_main_keyboard())
    await call.answer()


# --- Вспомогательная функция для самой рассылки ---
async def start_mailing(session: AsyncSession, bot: Bot, from_chat_id: int, message_id: int):
    user_ids = await crud.get_all_user_ids(session)
    sent_count = 0
    failed_count = 0

    for user_id in user_ids:
        try:
            await bot.copy_message(chat_id=user_id, from_chat_id=from_chat_id, message_id=message_id)
            sent_count += 1
            # ВАЖНО: Добавляем небольшую задержку, чтобы не получить бан от Telegram за флуд
            await asyncio.sleep(0.1) # 10 сообщений в секунду
        except Exception as e:
            failed_count += 1
            print(f"Не удалось отправить сообщение пользователю {user_id}: {e}")
    
    # Отправляем админу отчет о результатах
    await bot.send_message(
        from_chat_id,
        f"📢 Рассылка завершена!\n\n"
        f"✅ Отправлено: {sent_count}\n"
        f"❌ Не удалось отправить: {failed_count}"
    )