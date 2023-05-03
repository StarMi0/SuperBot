from aiogram import types, Dispatcher
from functions.functions import get_discount_code, key_dict
from create_bot import dp, bot
from keyboard import kb_client


# @dp.message_handler()
async def check_client(message: types.Message):
    user_id = message.from_user.id  # ID пользователя который запустил хэндлер
    # user_channel_status = await bot.get_chat_member(key_dict['tg_chanel'], user_id)
    # if user_channel_status["status"] == "left":
    if False:
        await bot.send_message(message.chat.id, f'Подпишитесь на наш канал: {key_dict["url_tg"]}\n,'
                                                f'чтобы получить купон и повторите попытку.')
    else:
        # Генерация и присылка купона:
        cupon_path = get_discount_code('tg', user_id)
        if cupon_path:
            photo = open(cupon_path, 'rb')
            await bot.send_photo(message.chat.id, photo=photo)
        else:
            await bot.send_message(message.chat.id, "У Вас уже есть активный купон.")


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, f"Если вы еще не получали скидочный купон, "
                                                     f"нажмите 'Получить купон' или введите команду /coupon",
                               reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply(f'Not in LS {message.chat.id}')


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start)
    dp.register_message_handler(check_client, commands=['coupon'])

