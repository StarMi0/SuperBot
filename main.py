from aiogram import executor
from Telegramm import bot, admin
from create_bot_tg import on_startup, dp

admin.register_handler_admin(dp)
bot.register_handler_client(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)

