from aiogram import types, Dispatcher
from functions.functions import get_discount_code, key_dict
from create_bot import dp, bot


def read_file_into_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content


async def add_to_db(message: types.Message):
    msg = message.text
    text_list = msg.split()
    if len(text_list) != 2:
        await bot.send_message(message.chat.id, 'Error: incorrect parameters')
    else:
        platform = text_list[1]
        if platform == 'vk':
            # Ask user for VK ID
            await bot.send_message(message.chat.id, 'Please enter the VK user ID')
            vk_id_msg = await bot.wait_for_message(chat_id=message.chat.id)

            # Add user to the list
            add_to_db(vk_id_msg.text)

        elif platform == 'tg':
            # Ask user for Telegram username
            await bot.send_message(message.chat.id, 'Please enter the Telegram username')
            tg_username_msg = await bot.wait_for_message(chat_id=message.chat.id)

            # Add user to the list
            add_to_db(tg_username_msg.text)

        else:
            await bot.send_message(message.chat.id, 'Error: incorrect platform')


async def get_qr(message: types.Message):
    pass


async def status(message: types.Message):
    pass


def register_handler_admin(dp: Dispatcher):

    dp.register_message_handler(check_client, text='Хочу купон')
    dp.register_message_handler(command_start, state='*', content_types=['text'])