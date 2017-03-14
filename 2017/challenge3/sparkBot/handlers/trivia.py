import os
import requests
from handler_base import MessageHandler
import json
import random
from operator import *

class Trivia(MessageHandler):
    def handle_message(self, raw_msg, user_email, username):
        if "triviaquestion" in str(raw_msg).lower():
            return self.get_trivia_question()
        if "triviaanswer" in str(raw_msg).lower():
            return self.get_trivia_answer()
        return False

    def help(self):
        return "**JeopradyTrivia** - Returns a randomly pulled jeoprady question"

    def get_trivia_question(self):
        r = requests.get('http://jservice.io/api/random')
        j = json.loads(r.text)
        category = str(j[0]['category']['title'])
        question = str(j[0]['question'])
        answer = str(j[0]['answer'])

        response_question = {'text': '>*Category: %s*\n\n>*Question: %s*' % (category, question)}
        response_answer =   {'text': '>*Answer: %s*' % (answer)}
        self.store_trivia_answer(response_answer)

        return str(response_question['text'])

    def get_trivia_answer(self):
        answer = ''
        if not os.path.isfile('sparkBot/handlers/data_files/trivia_answer.json'):
            return 'No Question'

        with open('sparkBot/handlers/data_files/trivia_answer.json') as json_file:
            answer = json.load(json_file)

        os.remove('sparkBot/handlers/data_files/trivia_answer.json')
        return str(answer['text'])

    def store_trivia_answer(self, response_answer):
        with open('sparkBot/handlers/data_files/trivia_answer.json', 'w') as json_file:
            json.dump(response_answer, json_file)

