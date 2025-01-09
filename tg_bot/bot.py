from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio

from src.config import TG_API
from tg_bot.auth_middleware import AuthMiddleware
from tg_bot.handlers.auth import router as auth_router

async def main():
    bot = Bot(token=TG_API, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    # Authentication process
    dp.message.middleware(AuthMiddleware())

    # Handlers
    dp.include_router(auth_router)


    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())
