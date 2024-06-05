from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.fsm.context import FSMContext
from aiogram.types import TelegramObject, User

from app.bot.manager import Manager
from app.texts import SUPPORTED_LANGUAGES


class ManagerMiddleware(BaseMiddleware):
    """
    Middleware for handling the manager object.
    """

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        """
        Call the middleware.

        :param handler: The handler function.
        :param event: The Telegram event.
        :param data: Additional data.
        """
        user: User = data.get("event_from_user")
        if user and not user.is_bot:
            await set_language_code(user, data)
            # Create a new manager object
            manager = Manager(data)
            # Pass the config data to the handler function
            data["manager"] = manager

            # Call the handler function with the event and data
        return await handler(event, data)


async def set_language_code(user: User, data: dict) -> None:
    state: FSMContext = data.get("state")
    state_data = await state.get_data()

    language_code = state_data.get("language_code")

    if not language_code:
        if user.language_code in SUPPORTED_LANGUAGES.keys():
            language_code = user.language_code
        else:
            language_code = "en"

    data["language_code"] = language_code
