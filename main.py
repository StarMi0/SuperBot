from aiogram import executor
from create_bot import dp, vk_session, vk, upload
from Telegramm import bot
from vk_api.bot_longpoll import VkBotLongPoll
from functions.functions import key_dict
from VK.vk import run_vk_bot


async def on_startup(_):
    print('Telegram bot is online')


bot.register_handler_client(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
    longpoll = VkBotLongPoll(vk_session, key_dict['VK_GROUP_ID'])
    print("VK bot is runned...")
    run_vk_bot(longpoll, vk, upload)
