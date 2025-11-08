from aiogram.fsm.state import StatesGroup, State

class QuizState(StatesGroup):
    # Состояние, в котором пользователь находится во время прохождения квиза
    in_game = State()