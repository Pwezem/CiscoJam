from handler_base import MessageHandler
import json
import random


class Numbers(MessageHandler):
    def __init__(self, path_to_file="handlers/data_files/eightball.json"):
        with open(path_to_file) as json_file:
            self.data = json.load(json_file)
        pass

    def handle_message(self, raw_msg, user_email, username):
        large_nums = [25, 50, 75, 100]
        small_nums = [1 , 1 , 2 , 2 , 3 , 3 , 4 , 4 , 5 , 5 , 6 , 6 , 7 , 7 , 8 , 8 , 9 , 9 , 10 , 10 ]

        if str(raw_msg).lower() == "numbers":
            return self.get_numbers(raw_msg[7::])
        return False

    def help(self):
        return "**numbers s: l:** - Returns numbers countdown game"

    def get_numbers(self, msg):
        response = "**Cancelling numbers game**<br>"
        items = msg.split(" ")
        small = 0
        large = 0
        target = self.get_three_digit_num()
        answer = 0
        for item in items:
            if "s:" in item.lower():
                small = self.get_num_from_string(item)
            if "l:" in item.lower():
                large = self.get_num_from_string(item)

        if large > 4:
            return response + "Large number is too big %d." % large
        if small > 6:
            return response + "Small number is too big %d." % small
        if (small+large)> 6:
            return response + "Combined numbers can't be greater then six<br>" \
                              "s:%d + l:%d > 6" %(small, large)

        return "656 djue"

    def get_three_digit_num(self):
        return random.randint(0, 999)

    def get_num_from_string(self, string):
        return int(string[2::])