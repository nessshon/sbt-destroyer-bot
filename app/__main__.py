import asyncio

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from pytonapi import AsyncTonapi
from redis.asyncio import Redis

from .bot.commands import (
    bot_commands_setup,
    bot_commands_delete,
)
from .bot.handlers import bot_routers_include
from .bot.middlewares import bot_middlewares_register
from .config import Config, load_config
from .logger import setup_logger


async def on_startup(
        dispatcher: Dispatcher,
        bot: Bot,
        config: Config,
        redis: Redis,
) -> None:
    """
    Startup event handler. This runs when the bot starts up.
    """
    bot_middlewares_register(
        dispatcher,
        redis=redis,
        config=config,
    )
    bot_routers_include(dispatcher)
    await bot_commands_setup(bot)


async def on_shutdown(bot: Bot) -> None:
    """
    Shutdown event handler. This runs when the bot shuts down.
    """
    await bot_commands_delete(bot)
    await bot.delete_webhook()
    await bot.session.close()


async def main() -> None:
    """
    Main function that initializes the bot and starts the event loop.
    """
    config = load_config()

    tonapi = AsyncTonapi(
        config.tonapi.KEY,
        max_retries=5,
    )

    storage = RedisStorage.from_url(
        url=config.redis.DSN,
    )
    bot = Bot(
        token=config.bot.TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        ),
    )
    dp = Dispatcher(
        bot=bot,
        storage=storage,
        config=config,
        redis=storage.redis,
        tonapi=tonapi,
    )

    # Register startup handler
    dp.startup.register(on_startup)
    # Register shutdown handler
    dp.shutdown.register(on_shutdown)

    # Start the bot
    await bot.delete_webhook()
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    # Setup logging
    setup_logger()
    # Run the bot
    asyncio.run(main())
