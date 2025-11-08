QUESTIONS = [
    {
        "text": "Какой метод используется для отправки сообщений в aiogram?",
        "options": ["send_message", "answer", "reply", "send"],
        "correct_answer": "send_message"
    },
    {
        "text": "Что такое FSM в контексте Telegram-ботов?",
        "options": ["Файловая Система Менеджмента", "Машина Конечных Состояний", "Фильтр Системных Сообщений"],
        "correct_answer": "Машина Конечных Состояний"
    },
    {
        "text": "Какой декоратор используется для обработки команды /start в aiogram 3.x?",
        "options": ["@dp.message_handler(commands=['start'])", "@router.message(Command('start'))", "@router.message(CommandStart())"],
        "correct_answer": "@router.message(CommandStart())"
    },
    {
        "text": "Как получить user_id пользователя из объекта Message?",
        "options": ["message.user.id", "message.chat.id", "message.from_user.id"],
        "correct_answer": "message.from_user.id"
    },
    {
        "text": "Какой тип клавиатуры исчезает после нажатия?",
        "options": ["ReplyKeyboardMarkup", "InlineKeyboardMarkup"],
        "correct_answer": "InlineKeyboardMarkup"
    }
]