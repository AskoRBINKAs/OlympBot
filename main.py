from aiogram import Bot, Dispatcher, F
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from handlers import *
import asyncio
import config
import logging
async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.MARKDOWN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.message.register(start_handler,Command(commands="start"))
    dp.message.register(main_loop)
    dp.callback_query.register(callback_subject)
    dp.callback_query.register(callback_classes)
    dp.callback_query.register(callback_levels)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())