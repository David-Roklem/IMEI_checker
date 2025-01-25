from aiogram.fsm.state import StatesGroup, State


class UserInputStates(StatesGroup):
    test_mode = State()
    prod_mode = State()
