from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
from app.config import CHANNEL_ID
from keyboards.reply import main_menu_keyboard

router = Router()

@router.callback_query(F.data == "check_subscription")
async def check_subscription_handler(call: CallbackQuery, bot: Bot):
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.from_user.id)
        if member.status in ["member", "administrator", "creator"]:
            # Если подписан, удаляем сообщение с кнопками и приветствуем
            await call.message.delete()
            await call.message.answer(
                "Отлично, вы подписаны! Теперь можно пользоваться ботом.",
                reply_markup=main_menu_keyboard()
            )
        else:
            # Если все еще не подписан
            await call.answer("Вы все еще не подписаны на канал.", show_alert=True)
    except Exception as e:
        await call.answer("Произошла ошибка при проверке подписки.", show_alert=True)
        print(f"Ошибка в check_subscription_handler для {call.from_user.id}: {e}")