from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    SELECT_LANGUAGE = State()
    CHANGE_LANGUAGE = State()

    MAIN_MENU = State()
    NFT_INFO = State()
