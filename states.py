from aiogram.fsm.state import default_state, State, StatesGroup


class FSMGetSearchArgs(StatesGroup):
    subjects = State()
    student_class = State()
    olymp_level = State()
