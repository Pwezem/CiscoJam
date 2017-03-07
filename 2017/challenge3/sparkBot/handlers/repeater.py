from handler_base import MessageHandler


class Repeater(MessageHandler):
    def __init__(self):
        pass

    def handle_message(self, raw_msg, user_email, username):
        """
            Repeats the message based on the command,
            The raw_msg should remove the command before it replies.

            all handle_message should return false if they can't be handled by this class.
        """
        if "repeat_message" in raw_msg.lower():
            return "**All I do is repeat:** " + raw_msg[14::]
        if "repeat_backwards" in raw_msg.lower():
            return "**Repeating your message backwards:** " + (raw_msg[::-1])[:-16].strip()
        return False

    def help(self):
        return "**repeat_message** - Repeats whatever message is sent.<br>" \
               "**repeat_backwards** - Repeats the message backwards."
