from aiogram import executor
from Telegramm import bot
from create_bot_tg import on_startup, dp
from create_bot_vk import run_vk
import asyncio

bot.register_handler_client(dp)

# ioloop = asyncio.get_event_loop()
# tasks = [
#     ioloop.create_task(executor.start_polling(dp, skip_updates=False, on_startup=on_startup)),
#     ioloop.create_task(longpoll),
#
# ]
#
#
# # 3 variance
#
# async def multiple_tasks():
#     res = await asyncio.gather(*tasks, return_exceptions=True)
#     return res


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)

    # ioloop.run_until_complete(asyncio.wait(tasks))
    # ioloop.close()
