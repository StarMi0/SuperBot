import re
import sqlite3

from aiogram.dispatcher import FSMContext

from .keyboard import kb_admin, kb_admin1
from aiogram import types, Dispatcher
from functions.functions import get_discount_code, key_dict
from create_bot_tg import dp, bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from functions.functions import add_to_db

conn = sqlite3.connect('code.db')
cursor = conn.cursor()


def read_file_into_list(filename):
    with open(filename) as f:
        content = re.findall(r'\d+', ''.join(f.readlines()))

    return content


admins = read_file_into_list('Telegramm/admin.txt')
sallers = read_file_into_list('Telegramm/sallers.txt')


class AdminStateGroup(StatesGroup):
    social = State()
    user_id = State()
    final = State()


async def add_user(message: types.Message):
    if str(message.from_user.id) in admins:
        await bot.send_message(message.from_user.id, "Выберите социальную сеть, в которую хотите добавить запись:",
                               reply_markup=kb_admin)
    await AdminStateGroup.social.set()


async def chose_id(message: types.Message, state: FSMContext):
    social = message.text
    async with state.proxy() as data:
        data["social"] = social
    await message.answer("Введите ID пользователя, которого хотите добавить в БД:")
    await AdminStateGroup.user_id.set()


async def final(message: types.Message, state: FSMContext):
    id_user = message.text
    async with state.proxy() as data:
        data["user_id"] = id_user

    await message.answer("Что нужно сделать?",
                         reply_markup=kb_admin1)
    await AdminStateGroup.final.set()


async def save_or_get(message: types.Message, state: FSMContext):
    data = await state.get_data()
    social = data.get("social")
    iser_id = data.get("user_id")
    if message.text == "add user" and str(message.from_user.id) in admins:
        add_to_db(social, iser_id, None)
        await bot.send_message(message.chat.id,
                               f"Данные записаны!")
    elif message.text == "get" and str(message.from_user.id) in sallers:
        cupon_path = get_discount_code(social, iser_id, True)
        photo = open(cupon_path, 'rb')
        await bot.send_photo(message.chat.id, photo=photo)
    else:
        await bot.send_message(message.chat.id,
                               f"Проверьте правильность ввода данных или наличие прав доступа:\n\n"
                               f"Социальная сеть: {social}\n"
                               f"ID пользователя: {iser_id}\n"
                               f"Добавлять записи может только администратор,\n"
                               f"Получать код повторно может только продавец.")
    await state.finish()


async def status(message: types.Message):
    if str(message.from_user.id) in admins:
        all_data = cursor.execute("SELECT COUNT(*) FROM USERS").fetchone()[0]
        vk_data = cursor.execute("SELECT COUNT(*) FROM USERS WHERE social = 'vk'").fetchone()[0]
        tg_data = cursor.execute("SELECT COUNT(*) FROM USERS WHERE social = 'tg'").fetchone()[0]
        text = f"Status: online;\n" \
               f"Всего выдано купонов: {all_data}\n" \
               f"Купонов Телеграмм: {tg_data}\n" \
               f"Купонов Вконтакте: {vk_data}"
        try:
            await bot.send_message(message.from_user.id, text)
            await message.delete()
        except:
            await message.reply(f'Ошибка соединения...')


async def cd_cansel(message: types.Message, state: FSMContext) -> None:
    current_state = state.get_state()
    if current_state is None:
        return
    await state.finish()


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(status, text='status')

    dp.register_message_handler(add_user, text='add', state=None)
    dp.register_message_handler(chose_id, state=AdminStateGroup.social)
    dp.register_message_handler(final, state=AdminStateGroup.user_id)
    dp.register_message_handler(save_or_get, state=AdminStateGroup.final)
