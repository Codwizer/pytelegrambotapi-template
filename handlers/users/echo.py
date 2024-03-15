from loader import bot
from telebot.types import Message


@bot.message_handler(func=lambda message: True)
def echo(message: Message):
    bot.send_message(message.chat.id, message.text)
