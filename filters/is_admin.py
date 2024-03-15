from tabnanny import check
from telebot.custom_filters import SimpleCustomFilter


class IsAdmin(SimpleCustomFilter):
    key = "is_admin"

    @staticmethod
    def filter(self, message):
        check = self.bot.get_chat_member(message.chat.id, message.from_user.id)
        if check.status == "administrator" or check.status == "creator":
            return True
        else:
            return False
