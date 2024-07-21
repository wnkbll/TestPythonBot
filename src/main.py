import asyncio

from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loguru import logger

from src.core.config import TOKEN
from src.db.db_redis import set_currencies
from src.routes import router


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    logger.success("Bot was connected")

    await set_currencies()

    scheduler = AsyncIOScheduler()
    scheduler.add_job(set_currencies, 'interval', hours=24, id='set_currencies_job')
    scheduler.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
