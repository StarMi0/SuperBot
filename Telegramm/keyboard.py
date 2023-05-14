from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

coupon = KeyboardButton('Хочу купон')

vk_button = KeyboardButton('vk')
tg_button = KeyboardButton('tg')

cansel_b = KeyboardButton('cansel')

add_user = KeyboardButton('add user')
get_dis = KeyboardButton('get')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_admin1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(coupon)
kb_admin.add(vk_button).add(tg_button).add(cansel_b)
kb_admin1.add(add_user).add(get_dis)