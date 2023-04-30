from aiogram import executor
from create_bot import dp
from Telegramm import bot
import sqlite3


async def on_startup(_):
    print('Telegram bot is online')


bot.register_handler_client(dp)

if __name__ == "__main__":
    executor.start_polling(dp)
