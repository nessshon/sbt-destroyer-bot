from dataclasses import dataclass
from pathlib import Path
from typing import Union

import environs

from environs import Env

BASE_DIR = Path(__file__).resolve().parent


@dataclass
class BotConfig:
    TOKEN: str
    DEV_ID: int


@dataclass
class RedisConfig:
    DSN: str


@dataclass
class TONAPIConfig:
    KEY: str
    TONCONNECT_KEY: Union[str, None]


@dataclass
class Config:
    bot: BotConfig
    redis: RedisConfig
    tonapi: TONAPIConfig

    MANIFEST_URL: str


def load_config() -> Config:
    env = Env()
    env.read_env()

    try:
        tonconnect_key = env.str("TONAPI_TONCONNECT_KEY", None)
    except environs.EnvValidationError:
        tonconnect_key = None

    return Config(
        bot=BotConfig(
            TOKEN=env.str("BOT_TOKEN"),
            DEV_ID=env.int("BOT_DEV_ID"),
        ),
        redis=RedisConfig(
            DSN=env.str("REDIS_DSN"),
        ),
        tonapi=TONAPIConfig(
            KEY=env.str("TONAPI_KEY"),
            TONCONNECT_KEY=tonconnect_key,
        ),
        MANIFEST_URL=env.str("MANIFEST_URL"),
    )
