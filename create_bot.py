import asyncio

from aiogram import Bot, Dispatcher, executor
from functions.functions import key_dict

bot = Bot(token=key_dict['TGID'])
dp = Dispatcher(bot)