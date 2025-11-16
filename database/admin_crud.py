from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta

from database.models import User

async def count_users(session: AsyncSession) -> int:
    """Считает общее количество пользователей."""
    q = select(func.count(User.user_id))
    result = await session.execute(q)
    return result.scalar()

async def count_new_users_for_period(session: AsyncSession, days: int) -> int:
    """Считает новых пользователей за указанный период (в днях)."""
    start_date = datetime.utcnow() - timedelta(days=days)
    q = select(func.count(User.user_id)).where(User.registration_date >= start_date)
    result = await session.execute(q)
    return result.scalar()

async def count_active_users_today(session: AsyncSession) -> int:
    """Считает пользователей, которые сегодня набрали очки (сыграли)."""
    q = select(func.count(User.user_id)).where(User.best_score > 0)
    result = await session.execute(q)
    return result.scalar()

async def get_weekly_winners(session: AsyncSession) -> list[User]:
    """Возвращает список пользователей, которые победили на этой неделе."""
    q = select(User).where(User.is_win == True)
    result = await session.execute(q)
    return result.scalars().all()


async def get_all_user_ids(session: AsyncSession) -> list[int]:
    """Возвращает список всех user_id из базы данных."""
    q = select(User.user_id)
    result = await session.execute(q)
    return result.scalars().all()