from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

from config_data.config import USERS_WHITELIST


class WhiteListMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        user: User = data.get("event_from_user")
        message = event.message
        if user is not None:
            user_id = user.id
            if user_id not in USERS_WHITELIST:
                await message.answer("У вас нет доступа к этому боту.")
                return

        result = await handler(event, data)

        return result
