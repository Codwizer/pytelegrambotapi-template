from loader import bot
from telebot.types import Message


@bot.message_handler(commands=["start"])
def command_start(message: Message):
    bot.send_message(message.chat.id, f"Salom, {message.from_user.full_name}")
