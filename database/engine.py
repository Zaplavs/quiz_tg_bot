from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
# --- Добавьте этот импорт ---
from database.models import Base

# Путь к нашей базе данных SQLite
DATABASE_URL = "sqlite+aiosqlite:///quiz_bot.db"

# Создаем асинхронный "движок" для подключения
# echo=True будет выводить в консоль все SQL-запросы, полезно для отладки
engine = create_async_engine(DATABASE_URL, echo=True)

# Фабрика сессий, которая будет создавать сессии для взаимодействия с БД
session_factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def create_tables():
    """
    Функция для создания всех таблиц в базе данных.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_tables():
    """
    Функция для удаления всех таблиц (для тестов).
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)