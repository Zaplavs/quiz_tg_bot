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

# --- Клавиатуры для админ-панели ---

def admin_main_keyboard() -> InlineKeyboardMarkup:
    """Главная клавиатура админ-панели."""
    builder = InlineKeyboardBuilder()
    builder.button(text="📊 Статистика и Информация", callback_data="admin:stats")
    # --- НОВАЯ КНОПКА ---
    builder.button(text="📢 Рассылка", callback_data="admin:broadcast_start")
    builder.adjust(1)
    return builder.as_markup()

# --- НОВАЯ КЛАВИАТУРА ---
def broadcast_confirm_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура для подтверждения или отмены рассылки."""
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Отправить", callback_data="admin:broadcast_confirm")
    builder.button(text="❌ Отмена", callback_data="admin:broadcast_cancel")
    builder.adjust(2) # Две кнопки в одном ряду
    return builder.as_markup()


def admin_stats_keyboard() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для раздела 'Статистика и Информация'.
    """
    builder = InlineKeyboardBuilder()
    
    # Кнопки для конкретных действий в этом разделе
    builder.button(text="📈 Общая статистика", callback_data="admin:general_stats")
    builder.button(text="🏆 Список победителей недели", callback_data="admin:weekly_winners")
    
    # Кнопка "Назад" для возврата в главное меню админки
    builder.button(text="⬅️ Назад", callback_data="admin:main")
    
    # Выстраиваем кнопки в один столбец
    builder.adjust(1)
    
    return builder.as_markup()