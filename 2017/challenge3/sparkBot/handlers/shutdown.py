from handler_base import MessageHandler
import random


class ShutDown(MessageHandler):
    def __init__(self):
        pass

    def handle_message(self, raw_msg, user_email, username):
        if raw_msg.lower() == "shutdown":
            if random.randint(0, 10) is not 2:
                print "Powering down skynet"
                exit(0)
            else:
                return "You wrote: Skynet take over the world"
        return False

    def help(self):
        return "shutdown - shuts down the bot."
