from loader import bot
from telebot.types import Message


@bot.message_handler(commands=["help"])
def command_help(message: Message):
    bot.send_message(message.chat.id, "Qanday yordam kerak?")
