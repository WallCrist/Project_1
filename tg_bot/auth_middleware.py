from aiogram import BaseMiddleware
from typing import Callable, Dict, Any, Awaitable
from aiogram.types import Message
import aiohttp


class AuthMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            message: Message,
            data: Dict[str, Any]) -> Any:

        username = message.from_user.username

        # TODO: Add a skip for register state and messages with register

        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://localhost:8000/users/username/{username}") as response:
                if response.status == 404:
                    await message.answer("<b>Please register first! Use /start</b>")
                    return

                user_data = await response.json()
                data["user"] = user_data

        return await handler(message, data)
