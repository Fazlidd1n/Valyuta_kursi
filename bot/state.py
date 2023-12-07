from aiogram.fsm.state import StatesGroup, State


class Menu(StatesGroup):
    menu = State()
    val = State()
    cal = State()
    reklama = State()
