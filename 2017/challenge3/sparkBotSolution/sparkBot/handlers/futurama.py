from handler_base import MessageHandler
import random
"""
    This is an example class for you to understand how the handlers work.
    Each new handler must extend MessageHandler class, override the handle_message
    and the help message.

"""

class Futurama(MessageHandler):
    def __init__(self):
        self.quotes = ["Bite my shiny metal ass!", "Shut up baby, I know it!",
                       "Hahahahaha. Oh wait you're serious. Let me laugh even harder.",
                       "You know what cheers me up? Other people's misfortune.",
                       "Anything less than immortality is a complete waste of time.",
                       "Blackmail is such an ugly word. I prefer extortion. The \"x\" makes it sound cool.",
                       "Have you tried turning off the TV, sitting down with your children, and hitting them?"]

    def handle_message(self, raw_msg, user_email, username):
        if "futurama" in raw_msg.lower():
            return random.choice(self.quotes)
        return False

    def help(self):
        return "**futurama** - Responds with a futurama quote"
