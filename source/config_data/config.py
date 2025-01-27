from dataclasses import dataclass
from environs import Env


@dataclass
class Config:
    bot_token: str
    token_api_sandbox: str
    token_api_live: str


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        bot_token=env('BOT_TOKEN'),
        token_api_sandbox=env('TOKEN_API_SANDBOX'),
        token_api_live=env('TOKEN_API_LIVE'),
    )


config: Config = load_config()

IMEI_CHECKER_BASE_URL = "https://api.imeicheck.net/"

CUSTOM_REQ_TIMEOUT = 20

USERS_WHITELIST = []
