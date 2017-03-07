from utils import *
import os
import requests
from handler_base import MessageHandler
import json
import random
from operator import *

#header = {'Authorization': general_info["authorization"]}
class JeopradyTrivia(MessageHandler):
    def __init__(self):
        print "init bruv"

    def handle_message(self, raw_msg, user_email, username):
        if "jeopradyquestion" in str(raw_msg).lower():
            return self.get_trivia_question()
        if "jeopradyanswer" in str(raw_msg).lower():
            return self.get_trivia_answer()
        return False

    def help(self):
        return "**JeopradyTrivia** - Returns a randomly pulled jeoprady question"

    def get_trivia_question():
        r = requests.get('http://jservice.io/api/random')
        j = json.loads(r.text)
        category = str(j[0]['category']['title'])
        question = str(j[0]['question'])
        answer = str(j[0]['answer'])

        response_question = {'text': 'Category: %s\n\nQuestion: %s' % (category, question),
                             'markdown': '>*Category: %s*\n\n>Question: %s' % (category, question)}
        response_answer =   {'text': 'Answer: %s' % answer,
                             'markdown': '>*Answer: %s' % (answer)}
        self.store_trivia_answer(response_answer)

        return response_question

    def get_trivia_answer(room_id):
        answer = ''
        if os.path.isfile('handlers/data_files/trivia_answer.json'):
            return 'No Question'

        with open('handlers/data_files/trivia_answer.json') as json_file:
            answer = json.load(json_file)

        os.remove('handlers/data_files/trivia_answer.json')

        return answer

    def store_trivia_answer(response_answer):
        with open('handlers/data_files/trivia_answer.json', 'w') as json_file:
            json_file.dump(answer)


# For testing without using bot
def main():
    JeopradyTrivia.handle_message('jeopradytrivia', 'tooneill@cisco.com', 'tooneill')

if __name__ == '__main__':
    main()