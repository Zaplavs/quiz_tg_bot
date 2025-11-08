import random
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def make_quiz_keyboard(options: list[str]) -> InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру с вариантами ответов для квиза.
    """
    builder = InlineKeyboardBuilder()
    # Перемешиваем варианты ответов для каждой новой клавиатуры
    random.shuffle(options)
    for option in options:
        # Для каждой кнопки `callback_data` будет содержать префикс "answer:" и сам текст ответа
        builder.button(text=option, callback_data=f"answer:{option}")
    # Выстраиваем кнопки в один столбец
    builder.adjust(1)
    return builder.as_markup()