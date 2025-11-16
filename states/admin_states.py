from aiogram.fsm.state import StatesGroup, State

class BroadcastState(StatesGroup):
    # Состояние, когда бот ожидает сообщение для рассылки
    waiting_for_message = State()
    # Состояние, когда бот ожидает подтверждения
    waiting_for_confirmation = State()