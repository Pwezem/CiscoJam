from handler_base import MessageHandler


class MeaningOfLife(MessageHandler):
    def __init__(self):
        pass

    def handle_message(self, raw_msg, user_email, username):
        """
            Checks if the "raw_msg" has the command "meaning of life".
            If so it returns the meaning of life
            Otherwise it returns False.
            HINT: remove "pass", to begin
            HINT: meaning of life is a hitchhikers guide to the galaxy.
            HINT: the test_meaningoflife_handler.py will assist you in completing
            this challenge.

            :param raw_msg: The message to preform operations on.
            :param user_email: email of the user.
            :param username: username of user who made the request.
            :return: String or False.
        """
        pass

    def help(self):
        return "**meaning of life** - Ask the bot what the meaning of life is"
