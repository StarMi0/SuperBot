from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

coupon = InlineKeyboardButton('👉КУПОН👈', callback_data="button")

kb_client = InlineKeyboardMarkup(resize_keyboard=True)

kb_client.add(coupon)
