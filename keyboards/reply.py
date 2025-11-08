from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main_menu_keyboard() -> ReplyKeyboardMarkup:
    """
    Создает клавиатуру главного меню.
    """
    builder = ReplyKeyboardBuilder()

    # Добавляем кнопки в несколько рядов
    builder.row(
        KeyboardButton(text="Начать игру 🚀")
    )
    builder.row(
        KeyboardButton(text="Профиль 👤"),
        KeyboardButton(text="Рейтинг 🏆")
    )
    builder.row(
        KeyboardButton(text="Призы 🎁"),
        KeyboardButton(text="Правила игры 📜")
    )
    builder.row(KeyboardButton(text="Пригласить друга 🤝"))

    # as_markup() возвращает готовый объект клавиатуры
    # resize_keyboard=True делает кнопки более компактными
    return builder.as_markup(resize_keyboard=True)