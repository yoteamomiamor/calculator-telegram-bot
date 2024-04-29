from dataclasses import dataclass
from environs import Env
from typing import Optional


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    bot: TgBot


def load_config(path: Optional[str] = None) -> Config:
    env = Env()
    env.read_env(path=path)
    return Config(bot=TgBot(token=env('BOT_TOKEN')))
