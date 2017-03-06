from handler_base import MessageHandler


class MeaningOfLife(MessageHandler):
    def __init__(self):
        pass

    def handle_message(self, raw_msg, user_email, username):
        if "meaning of life" in raw_msg:
            return "42 %s" % username
        return False

    def help(self):
        return "**meaning of life** - Ask the bot what the meaning of life is"
