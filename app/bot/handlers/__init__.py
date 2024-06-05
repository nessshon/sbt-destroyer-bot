from aiogram import Dispatcher
from aiogram_tonconnect.handlers import AiogramTonConnectHandlers

from . import private
from . import errors


def bot_routers_include(dp: Dispatcher) -> None:
    """
    Include bot routers.
    """
    dp.include_routers(
        *[
            private.command.router,
        ],
    )

    AiogramTonConnectHandlers().register(dp)

    dp.include_routers(
        *[
            errors.router,
            private.callback_query.router,
            private.message.router,
        ]
    )


__all__ = [
    "bot_routers_include",
]
