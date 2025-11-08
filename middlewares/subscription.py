from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject, Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from app.config import CHANNEL_ID

def check_subscription_keyboard() -> InlineKeyboardMarkup:
    """Создает клавиатуру с кнопками 'Подписаться' и 'Проверить подписку'."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Подписаться", url=f"https://t.me/+B3sLVudXTa5hMWVi")],
        [InlineKeyboardButton(text="🔄 Проверить подписку", callback_data="check_subscription")]
    ])

class CheckSubscriptionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        # Проверяем, что событие от пользователя (Message или CallbackQuery)
        if isinstance(event, (Message, CallbackQuery)):
            user = event.from_user
            bot: Bot = data.get('bot')

            # Пропускаем команду /start и callback проверки подписки, чтобы не было цикла
            if isinstance(event, Message) and event.text and event.text.startswith("/start"):
                return await handler(event, data)
            if isinstance(event, CallbackQuery) and event.data == "check_subscription":
                return await handler(event, data)

            try:
                member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user.id)
                # Пользователь подписан, если его статус 'member', 'administrator' или 'creator'
                if member.status in ["member", "administrator", "creator"]:
                    return await handler(event, data) # Пропускаем дальше
                else:
                    # Пользователь не подписан
                    await event.answer(
                        "Для использования бота необходимо подписаться на наш канал.",
                        reply_markup=check_subscription_keyboard()
                    )
            except Exception as e:
                # Если бот не может проверить (например, пользователь заблокировал его)
                print(f"Ошибка проверки подписки для {user.id}: {e}")
                await event.answer(
                    "Не удалось проверить вашу подписку. Убедитесь, что вы не заблокировали бота и попробуйте снова.",
                    reply_markup=check_subscription_keyboard()
                )
        else:
            return await handler(event, data)