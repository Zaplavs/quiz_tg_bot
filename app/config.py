import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем токен бота. Если токен не найден, будет ошибка.
BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')
CHANNEL_ID = os.getenv('CHANNEL_ID')

if not BOT_TOKEN:
    print("Ошибка: Не найден токен бота. Убедитесь, что он указан в файле .env")
    exit()