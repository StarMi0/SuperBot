from aiogram import executor
from Telegramm import bot
from create_bot_tg import on_startup, dp
from create_bot_vk import run_vk
import asyncio

bot.register_handler_client(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)


