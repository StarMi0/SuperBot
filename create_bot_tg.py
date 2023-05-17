import asyncio

from aiogram import Bot, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage

from create_bot_vk import run_vk
from functions.functions import key_dict

# Connect to Telegramm API
bot = Bot(token=key_dict['TGID'])
dp = Dispatcher(bot, storage=MemoryStorage())


async def on_startup(_):
    # asyncio.create_task(run_vk())
    print('Telegram bot is online')











