from aiogram import executor
from Telegramm import bot, admin
from create_bot_tg import on_startup, dp
from create_bot_vk import run_vk
import asyncio


admin.register_handler_admin(dp)
bot.register_handler_client(dp)


async def run_TG():
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
    print("TG bot is online!!!")


ioloop = asyncio.get_event_loop()
tasks = [
    ioloop.create_task(executor.start_polling(dp, skip_updates=False, on_startup=on_startup)),
    ioloop.create_task(run_vk())
]

if __name__ == "__main__":
    ioloop.run_until_complete(asyncio.wait(tasks))

