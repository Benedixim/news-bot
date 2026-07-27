from aiogram.fsm.state import State, StatesGroup


class Survey(StatesGroup):

    course = State()

    specialization = State()

    price = State()

    location = State()

    language = State()
