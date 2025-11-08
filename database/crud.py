from sqlalchemy import select, update # <-- Убедитесь, что 'update' импортирован
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import User

async def get_or_create_user(session: AsyncSession, user_id: int, full_name: str, username: str | None) -> tuple[User, bool]:
    """
    Получает пользователя из БД или создает нового.
    Возвращает кортеж: (объект User, был_ли_создан_bool).
    """
    stmt = select(User).where(User.user_id == user_id)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    
    if user:
        return user, False # Пользователь найден, не новый
    
    new_user = User(user_id=user_id, full_name=full_name, username=username)
    session.add(new_user)
    await session.commit()
    return new_user, True # Пользователь создан, новый

# --- ВОТ НОВЫЙ КОД, КОТОРЫЙ НУЖНО ДОБАВИТЬ ---

async def reset_all_scores(session: AsyncSession):
    """
    Обнуляет лучший результат (best_score) для всех пользователей.
    Это эквивалент SQL-запроса: UPDATE users SET best_score = 0;
    """
    stmt = update(User).values(best_score=0)
    await session.execute(stmt)
    await session.commit()
    # Эта строка нужна для отладки, чтобы вы видели в консоли, что задача выполнилась
    print("INFO: Weekly scores have been reset.") 

async def refresh_daily_attempts(session: AsyncSession):
    """
    Восстанавливает ежедневные попытки до 3 тем пользователям, у кого их меньше.
    Эквивалент: UPDATE users SET attempts_left = 3 WHERE attempts_left < 3;
    """
    stmt = (
        update(User)
        .where(User.attempts_left < 3)
        .values(attempts_left=3)
    )
    await session.execute(stmt)
    await session.commit()
    # Эта строка нужна для отладки
    print("INFO: Daily attempts have been refreshed.")

async def get_top_users(session: AsyncSession, limit: int = 10) -> list[User]:
    """
    Получает топ-N пользователей, отсортированных по best_score.
    """
    # Создаем запрос для выбора пользователей
    stmt = (
        select(User)
        .where(User.best_score > 0)  # Исключаем тех, у кого 0 очков
        .order_by(User.best_score.desc()) # Сортируем по очкам (по убыванию)
        .limit(limit) # Ограничиваем количество результатов
    )
    
    result = await session.execute(stmt)
    # .scalars().all() вернет список объектов User
    return result.scalars().all()

async def decrease_user_attempts(session: AsyncSession, user_id: int):
    """Уменьшает количество попыток пользователя на 1."""
    stmt = (
        update(User)
        .where(User.user_id == user_id, User.attempts_left > 0)
        .values(attempts_left=User.attempts_left - 1)
    )
    await session.execute(stmt)
    await session.commit()

async def update_user_best_score(session: AsyncSession, user_id: int, new_score: int):
    """Обновляет лучший счет пользователя, если новый счет выше."""
    stmt = (
        update(User)
        # Обновляем только если new_score > текущего best_score
        .where(User.user_id == user_id, User.best_score < new_score)
        .values(best_score=new_score)
    )
    await session.execute(stmt)
    await session.commit()


async def add_referral_attempt(session: AsyncSession, user_id: int):
    """
    Добавляет одну дополнительную попытку пользователю.
    """
    stmt = (
        update(User)
        .where(User.user_id == user_id)
        .values(attempts_left=User.attempts_left + 1)
    )
    await session.execute(stmt)
    await session.commit()