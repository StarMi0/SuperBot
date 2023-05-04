from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

coupon = KeyboardButton('Хочу купон')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(coupon)