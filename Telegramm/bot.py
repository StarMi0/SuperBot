import os.path

from aiogram import types, Dispatcher
from functions.functions import get_discount_code, key_dict
from create_bot_tg import dp, bot
from .keyboard import kb_client


async def check_client(message: types.Message):
    user_id = message.from_user.id  # ID пользователя который запустил хэндлер

    if False:
        await bot.send_message(message.chat.id, f'Для продления работы бота, оформите подписку')
        await message.delete()
    else:
        # Генерация и присылка купона:

        await bot.send_message(message.chat.id, "Для продления работы бота, оформите подписку")
        await message.delete()


async def callback_client(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id  # ID пользователя который запустил хэндлер

    if False:
        await bot.send_message(callback_query.from_user.id, f'Для продления работы бота, оформите подписку')
    else:
        # Генерация и присылка купона:

        await bot.send_message(callback_query.from_user.id, "Для продления работы бота, оформите подписку")


async def command_start(message: types.Message):
    user_name = message.from_user.full_name

    try:
        with open (os.path.join('media', 'new_message.jpg'), 'rb') as f:
            greeting_photo = f.read()
        await bot.send_photo(message.from_user.id, caption=f"Для продления работы бота, оформите подписку",
                             photo=greeting_photo,
                             reply_markup=kb_client)
        await message.delete()
    except ValueError as err:
        dict_response = {
            'error': err.args[0],
        }
        await message.reply(f'Ошибка соединения...\n{dict_response}')


def register_handler_client(dp: Dispatcher):
    dp.register_callback_query_handler(
        callback_client,
        lambda callback_query: True
    )
    dp.register_message_handler(check_client, text='КУПОН')
    dp.register_message_handler(command_start, state='*', content_types=['text'])
