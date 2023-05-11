import asyncio

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from aiogram import Bot, Dispatcher, executor
from functions.functions import key_dict

# Connect to Telegramm API
bot = Bot(token=key_dict['TGID'])
dp = Dispatcher(bot)


# Connect to VK API
GROUP_ID = 'https://vk.com/public220033168'  # Replace with your group ID
vk_session = vk_api.VkApi(token=key_dict['VKID'])

vk = vk_session.get_api()
upload = vk_api.VkUpload(vk)