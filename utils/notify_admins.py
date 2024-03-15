from loader import bot
from data.config import ADMINS


def notify_admins(message):
    try:
        for admin in ADMINS:
            bot.send_message(admin, message)
    except Exception as e:
        pass
