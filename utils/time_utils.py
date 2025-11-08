from datetime import datetime, timedelta, time
import pytz

def get_time_until_next_midnight() -> str:
    """
    Вычисляет и форматирует время до следующей полуночи по МСК.
    """
    # Устанавливаем часовой пояс Москвы
    moscow_tz = pytz.timezone("Europe/Moscow")
    
    # Получаем текущее время в Москве
    now = datetime.now(moscow_tz)
    
    # Определяем дату завтрашнего дня
    tomorrow_date = (now + timedelta(days=1)).date()
    
    # Время следующего сброса - это 00:00 завтрашнего дня
    next_reset_time = moscow_tz.localize(
        datetime.combine(tomorrow_date, time(0, 0))
    )

    # Вычисляем оставшееся время
    time_left = next_reset_time - now

    # Форматируем результат (здесь дни нам не нужны, т.к. их всегда 0)
    hours = time_left.seconds // 3600
    minutes = (time_left.seconds % 3600) // 60

    return f"{hours} ч. {minutes} мин."