from main import bot
from telebot.types import Message, BotCommand


def set_my_commands():
    bot.set_my_commands(
        [
            BotCommand("start", "Начало"),
            BotCommand("help", "Помощь"),
        ]
    )
