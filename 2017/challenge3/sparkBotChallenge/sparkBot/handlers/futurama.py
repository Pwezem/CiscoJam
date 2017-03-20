from handler_base import MessageHandler
import random
"""
    This is an example class for you to understand how the handlers work.
    Each new handler must extend MessageHandler class, override the handle_message
    and the help message.

"""
quotes = ["Bite my shiny metal ass!", "Shut up baby, I know it!",
          "Hahahahaha. Oh wait you're serious. Let me laugh even harder.",
          "You know what cheers me up? Other people's misfortune.",
          "Anything less than immortality is a complete waste of time.",
          "Blackmail is such an ugly word. I prefer extortion. The \"x\" makes it sound cool.",
          "Have you tried turning off the TV, sitting down with your children, and hitting them?"]


class Futurama(MessageHandler):
    def __init__(self):
        pass

    def handle_message(self, raw_msg, user_email, username):
        """
            Checks if the "raw_msg" has the command futurama.
            If so it returns a random quote from the list of "quotes" above
            Otherwise it returns False.
            HINT: remove "pass", to begin
            HINT: the test_futurama_handler.py will assist you in completing
            this challenge.

            :param raw_msg: The message to preform operations on.
            :param user_email: email of the user.
            :param username: username of user who made the request.
            :return: String or False.
        """
        pass

    def help(self):
        return "**futurama** - Responds with a futurama quote"
