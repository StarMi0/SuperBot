from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

coupon = KeyboardButton('/coupon')


kb_client = ReplyKeyboardMarkup()

kb_client.add(coupon)