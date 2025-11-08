from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy.ext.asyncio import async_sessionmaker

# Импортируем CRUD-функции
from database.crud import get_top_users, reset_all_scores, refresh_daily_attempts
# Импортируем ID админа из конфига
from app.config import ADMIN_ID


async def process_daily_results_and_reset(session_factory: async_sessionmaker, bot: Bot):
    """
    Определяет победителей, уведомляет их и админа, а затем сбрасывает очки.
    """
    async with session_factory() as session:
        # 1. Получаем топ-3 игроков за прошедший день
        winners = await get_top_users(session, limit=3)

        if winners:
            admin_message = "🏆 Ежедневные победители:\n\n"
            medals = ["🥇", "🥈", "🥉"]
            
            # 2. Проходим по списку победителей
            for i, winner in enumerate(winners):
                place = medals[i]
                # Формируем сообщение для админа
                admin_message += (
                    f"{place} {winner.full_name} (@{winner.username or 'N/A'}, "
                    f"ID: {winner.user_id}) - {winner.best_score} очков\n"
                )
                
                # 3. Отправляем уведомление победителю
                try:
                    await bot.send_message(
                        chat_id=winner.user_id,
                        text=f"🎉 Поздравляем, {winner.full_name}!\n\n"
                             f"Вы заняли <b>{i+1}-е место</b> в ежедневном квизе и выиграли приз! "
                             f"Автор скоро свяжется с вами для его вручения."
                    )
                except Exception as e:
                    print(f"Не удалось отправить сообщение пользователю {winner.user_id}: {e}")
            
            # 4. Отправляем итоговое уведомление админу
            if ADMIN_ID:
                await bot.send_message(ADMIN_ID, admin_message)
            else:
                print("ADMIN_ID не указан в .env, уведомление админу не отправлено.")
        
        # 5. Сбрасываем очки для всех
        await reset_all_scores(session)
        # print("Ежедневные результаты обработаны, очки сброшены.")


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

    scheduler.start()
    # print("Scheduler has been started.")