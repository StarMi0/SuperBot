import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import message

from create_bot_vk import run_vk


from aiogram.contrib.fsm_storage.memory import MemoryStorage
from functions.functions import key_dict

# Connect to Telegramm API
bot = Bot(token=key_dict['TGID'])
dp = Dispatcher(bot, storage=MemoryStorage())


loop = asyncio.get_event_loop()


async def on_startup(_):
    # asyncio.create_task(run_vk())
    print('Telegram bot is online')











