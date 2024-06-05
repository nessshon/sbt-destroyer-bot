from aiogram import Dispatcher
from aiogram_tonconnect.middleware import AiogramTonConnectMiddleware
from aiogram_tonconnect.tonconnect.storage.base import ATCRedisStorage
from aiogram_tonconnect.utils.qrcode import QRUrlProvider
from redis.asyncio import Redis

from .manager import ManagerMiddleware
from .throttling import ThrottlingMiddleware
from ..utils.keyboards import AiogramTonconnectInlineKeyboard
from ...config import Config


def bot_middlewares_register(dp: Dispatcher, **kwargs) -> None:
    """
    Register bot middlewares.
    """
    redis: Redis = kwargs["redis"]
    config: Config = kwargs["config"]

    dp.update.outer_middleware.register(
        AiogramTonConnectMiddleware(
            storage=ATCRedisStorage(redis),
            manifest_url=config.MANIFEST_URL,
            inline_keyboard=AiogramTonconnectInlineKeyboard,
            qrcode_provider=QRUrlProvider(),
            tonapi_token=config.tonapi.TONCONNECT_KEY,
            redirect_url="https://t.me/SBTDestroyerBot",
        )
    )

    dp.update.outer_middleware.register(ThrottlingMiddleware())
    dp.update.outer_middleware.register(ManagerMiddleware())


__all__ = [
    "bot_middlewares_register",
]
