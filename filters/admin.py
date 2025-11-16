from aiogram.filters import BaseFilter
from aiogram.types import Message
from app.config import ADMIN_ID

class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        # ADMIN_ID должен быть числом, поэтому приводим к строке для сравнения
        return str(message.from_user.id) == ADMIN_ID