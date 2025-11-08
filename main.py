import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from app.config import BOT_TOKEN
from handlers import common, quiz, service   # Импортируем роутер из common.py
from database.engine import create_tables, session_factory
from middlewares.db import DatabaseSessionMiddleware
from middlewares.subscription import CheckSubscriptionMiddleware 

from services.scheduler import setup_scheduler

async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

    # Создаем таблицы в БД при запуске
    await create_tables()

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    # --- Регистрируем middleware ---
    # Этот middleware будет создавать сессию для каждого обработчика
    dp.update.middleware(DatabaseSessionMiddleware(session_pool=session_factory))
    dp.message.middleware(CheckSubscriptionMiddleware())
    dp.callback_query.middleware(CheckSubscriptionMiddleware())

    dp.include_router(service.router)
    dp.include_router(common.router)
    dp.include_router(quiz.router)

    # Передаем ему фабрику сессий, чтобы он мог работать с БД
    setup_scheduler(session_factory, bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот остановлен.")