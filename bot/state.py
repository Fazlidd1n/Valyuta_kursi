from aiogram.fsm.state import StatesGroup, State


class Menu(StatesGroup):
    menu = State()
    val = State()
    type = State()
    cal = State()
    reklama = State()
