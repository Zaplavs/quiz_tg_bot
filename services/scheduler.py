from aiogram import Bot
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy.ext.asyncio import async_sessionmaker

# Импортируем CRUD-функции
from database.crud import get_top_users, reset_all_scores, refresh_daily_attempts, reset_weekly_win_status, get_daily_winners
# Импортируем ID админа из конфига
from app.config import ADMIN_ID


async def reset_win_status_job(session_factory: async_sessionmaker):
    """Задача для сброса статуса 'is_win' каждую неделю."""
    logging.info("Starting weekly win status reset...")
    try:
        async with session_factory() as session:
            await reset_weekly_win_status(session)
        logging.info("Weekly win statuses have been reset successfully.")
    except Exception as e:
        logging.error(f"An error occurred during weekly win status reset: {e}", exc_info=True)


async def process_daily_results_and_reset(session_factory: async_sessionmaker, bot: Bot):
    """
    Определяет победителей (которые еще не выигрывали), уведомляет их,
    обновляет их статус is_win, а затем сбрасывает очки.
    """
    logging.info("Starting daily results processing...")
    try:
        async with session_factory() as session:
            # 1. ИСПОЛЬЗУЕМ НОВУЮ ФУНКЦИЮ
            # Вместо get_top_users вызываем get_daily_winners, которая ищет игроков с is_win = False
            winners = await get_daily_winners(session)

            if winners:
                admin_message = "🏆 Ежедневные победители:\n\n"
                medals = ["🥇", "🥈", "🥉"]
                
                for i, winner in enumerate(winners):
                    # 2. ОБНОВЛЯЕМ СТАТУС ПОБЕДИТЕЛЯ
                    # Сразу после определения победителя, меняем его статус в объекте
                    winner.is_win = True
                    # И добавляем измененный объект в сессию, чтобы SQLAlchemy отслеживал это изменение
                    session.add(winner)
                    
                    # --- Остальная логика остается прежней ---
                    place = medals[i]
                    admin_message += (
                        f"{place} {winner.full_name} (@{winner.username or 'N/A'}, "
                        f"ID: {winner.user_id}) - {winner.best_score} очков\n"
                    )
                    try:
                        await bot.send_message(
                            chat_id=winner.user_id,
                            text=f"🎉 Поздравляем, {winner.full_name}!\n\n"
                                 f"Вы заняли <b>{i+1}-е место</b> в ежедневном квизе и выиграли приз! "
                                 f"Автор скоро свяжется с вами для его вручения."
                        )
                    except Exception as e:
                        logging.error(f"Не удалось отправить сообщение победителю {winner.user_id}: {e}")
                
                if ADMIN_ID:
                    await bot.send_message(ADMIN_ID, admin_message)

                # 3. СОХРАНЯЕМ ИЗМЕНЕНИЯ СТАТУСОВ
                # Делаем commit, чтобы записать в базу данных, что эти пользователи теперь победители (is_win = True)
                await session.commit()
            
            # 4. Сбрасываем очки для всех (это действие не изменилось)
            await reset_all_scores(session)
            logging.info("Daily results processed and scores reset successfully.")
    except Exception as e:
        logging.error(f"An error occurred during daily reset: {e}", exc_info=True)


async def refresh_attempts_job(session_factory: async_sessionmaker):
    """Задача для обновления ежедневных попыток (остается без изменений)."""
    async with session_factory() as session:
        await refresh_daily_attempts(session)


def setup_scheduler(session_factory: async_sessionmaker, bot: Bot):
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

    # Ежедневное обновление попыток в 00:00
    scheduler.add_job(refresh_attempts_job, 'cron', hour=0, minute=0, args=[session_factory])
    
    # Ежедневная обработка результатов и сброс очков в 00:00
    # Эта задача будет выполняться одновременно с обновлением попыток
    scheduler.add_job(
        process_daily_results_and_reset, 
        'cron', 
        hour=0, 
        minute=0, 
        args=[session_factory, bot] # Передаем сюда bot
    )

    scheduler.add_job(
        reset_win_status_job,
        trigger='cron',
        day_of_week='mon',
        hour=0,
        minute=5,
        args=[session_factory]
    )

    scheduler.start()
    # print("Scheduler has been started.")