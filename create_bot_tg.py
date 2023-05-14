from aiogram import Bot, Dispatcher


from aiogram.contrib.fsm_storage.memory import MemoryStorage
from functions.functions import key_dict

# Connect to Telegramm API
bot = Bot(token=key_dict['TGID'])
dp = Dispatcher(bot, storage=MemoryStorage())


async def on_startup(_):
    print('Telegram bot is online')











