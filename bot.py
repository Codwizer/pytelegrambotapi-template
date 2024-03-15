from telebot import TeleBot
from data.config import TOKEN
import utils
import handlers

bot = TeleBot(TOKEN)


def on_startup():
    utils.notify_admins("Start Bot")
    utils.set_my_commands()
    bot.infinity_polling(skip_pending=True)


on_startup()
