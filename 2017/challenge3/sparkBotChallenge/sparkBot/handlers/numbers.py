from handler_base import MessageHandler
import json
import random
from operator import *



class Numbers(MessageHandler):
    def __init__(self):
        self.large_nums = [25, 50, 75, 100]
        self.small_nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
        self.numbers = list()
        self.target = 0

    def handle_message(self, raw_msg, user_email, username):
        if "numbers" in str(raw_msg).lower():
            return self.get_numbers(raw_msg[8::].strip())
        return False

    def help(self):
        return "**numbers s: l:** - Returns numbers countdown game"

    def get_numbers(self, msg):
        """
            This method should check if "msg" contains next parts of the numbers commands.
            "msg" should contain a "l:<number>" and "s:<number>", if it's missing one or both
            of them this method should return a failing string.

            If "l:" is greater than 4, a fail string should be returned.
            If "s:" is greater than 6, a fail string should be returned.
            If the combined numbers of "l:" and "s:" are not equal to six,
            a fail string should be returned.

            If all is correct, this method should,
            choose "s:" random numbers from the "self.small_nums" list
            and "l:" random numbers from the self.large_nums" list.
            It should also return a "Target" 3 digit number to be reached.

            HINT: remove "pass" this is the countdown numbers game.
            HINT: test_numbers_handler.py will assist you in this challenge, look at the "expected_response"
            strings.
            HINT: there is also a fully functional bot that you can use to see how the game works.
            HINT: there are methods that will help you

            :param msg: Message containing the command and s: and l:
            :return: a string which is either a fail or a game.
        """
        pass

    def write_to_json_for_test(self):
        with open("handlers/data_files/numbers.json") as json_file:
            pass

    def get_three_digit_num(self):
        return random.randint(100, 999)

    def get_num_from_string(self, string):
        return int(string[2::])

    def pick_random_x(self, num, item_list):
        for i in range(num):
            random.shuffle(item_list)
            self.numbers.append(item_list.pop())
