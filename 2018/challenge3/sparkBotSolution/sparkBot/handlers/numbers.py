from handler_base import MessageHandler
import random



class Numbers(MessageHandler):
    def __init__(self):
        self.large_nums = [25, 50, 75, 100]
        self.small_nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
        self.numbers = list()
        self.target = 0

    def handle_message(self, raw_msg, user_email, username):
        if "numbers solve" in str(raw_msg).lower():
            return self.solve_numbers_game()
        if "numbers" in str(raw_msg).lower():
            return self.get_numbers(raw_msg[8::].strip())
        return False

    def help(self):
        return "**numbers s: l:** - Returns numbers countdown game"

    def get_numbers(self, msg):
        response = "**Cancelling numbers game**<br>"
        items = msg.split(" ")

        small = 0
        large = 0
        self.target = self.get_three_digit_num()

        for item in items:
            if "s:" in item.lower():
                small = self.get_num_from_string(item)
            elif "l:" in item.lower():
                large = self.get_num_from_string(item)
            else:
                return response + "No options supplied."

        if large > 4:
            return response + "Large number is too big %d." % large
        if small > 6:
            return response + "Small number is too big %d." % small
        if (small+large) > 6:
            return response + "Combined numbers can't be greater than six<br>" \
                              "s:%d + l:%d > 6" % (small, large)
        if (small+large) < 6:
            return response + "Combined numbers were less than six<br>" \
                              "s:%d + l:%d < 6" % (small, large)
        self.pick_random_x(small, self.small_nums)
        self.pick_random_x(large, self.large_nums)

        response = "**Numbers Game**<br>**Target:** %d<br>" \
                   "**Numbers:** %d, %d, %d, %d, %d, %d" \
                   % (self.target, self.numbers[0], self.numbers[1], self.numbers[2],
                      self.numbers[3], self.numbers[4], self.numbers[5])
        return response

    def solve_numbers_game(self, N, T):
        return "not implemented yet"

    def get_three_digit_num(self):
        return random.randint(100, 999)

    def get_num_from_string(self, string):
        return int(string[2::])

    def pick_random_x(self, num, item_list):
        for i in range(num):
            random.shuffle(item_list)
            self.numbers.append(item_list.pop())
