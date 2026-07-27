import asyncio
import os

from aiogram import Bot
from aiogram import Dispatcher

from bot.handlers import router




from dotenv import load_dotenv

load_dotenv()




TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(TOKEN)

dp = Dispatcher()

dp.include_router(router)


async def main():

    await dp.start_polling(bot)


if __name__ == "__main__":

    asyncio.run(main())