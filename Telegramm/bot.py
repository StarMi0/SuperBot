from aiogram import types, Dispatcher
from functions.functions import get_discount_code, key_dict
from create_bot_tg import dp, bot
from .keyboard import kb_client


async def check_client(message: types.Message):
    user_id = message.from_user.id  # ID пользователя который запустил хэндлер

    if False:
        await bot.send_message(message.chat.id, f'Подпишитесь на наш канал: {key_dict["url_tg"]}\n,'
                                                f'чтобы получить купон и повторите попытку.')
        await message.delete()
    else:
        # Генерация и присылка купона:
        cupon_path = get_discount_code('tg', user_id)
        if cupon_path:
            photo = open(cupon_path, 'rb')
            await bot.send_photo(message.chat.id, photo=photo)
        else:
            await bot.send_message(message.chat.id, "У Вас уже есть активный купон.")
        await message.delete()


async def callback_client(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id  # ID пользователя который запустил хэндлер

    if False:
        await bot.send_message(callback_query.from_user.id, f'Подпишитесь на наш канал: {key_dict["url_tg"]}\n,'
                                                            f'чтобы получить купон и повторите попытку.')
    else:
        # Генерация и присылка купона:
        cupon_path = get_discount_code('tg', user_id)
        if cupon_path:
            photo = open(cupon_path, 'rb')
            await bot.send_photo(callback_query.from_user.id, photo=photo)
        else:
            await bot.send_message(callback_query.from_user.id, "У Вас уже есть активный купон.")


async def command_start(message: types.Message):
    user_name = message.from_user.full_name
    try:
        await bot.send_message(message.from_user.id, f"Привет, {user_name}!\n"
                                                     f"Я бот Наша Обувь.\n"
                                                     f"Чтобы получить купон 500 руб, нажми\n"
                                                     f"КУПОН",
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
