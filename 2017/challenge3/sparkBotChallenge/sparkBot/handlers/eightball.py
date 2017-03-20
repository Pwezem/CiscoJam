from handler_base import MessageHandler
import json
import random


class Eightball(MessageHandler):
    
    def __init__(self, path_to_file="handlers/data_files/eightball.json"):
        with open(path_to_file) as json_file:
            self.data = ""
    
    def handle_message(self, raw_msg, user_email, username):
        """
            Checks if the "raw_msg" has the command eightball.
            If so it returns a random prediction from the list of predictions
            in the json file above, "path_to_file".
            Otherwise it returns false.
            HINT: remove "pass", to begin
            HINT: self.data is a holder for the json.
            HINT: the test_eightball_handler.py will assist you in completing
            this challenge.

            :param raw_msg: The message to preform operations on.
            :param user_email: email of the user.
            :param username: username of user who made the request.
            :return: String or False.
        """
        pass

    def help(self):
        return "**eightball** - Get a prediction"
