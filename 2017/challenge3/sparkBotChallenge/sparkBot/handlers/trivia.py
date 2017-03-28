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

    def get_trivia_question(self, path_to_file="data_files/trivia_answer.json"):
        """
            This method should make a request to "http://jservice.io/api/random"
            for a random trivia question.
            The request comes back wit a json object, within the object is a
            question, a title and an answer, the anwser needs to be stored in a
            seperate json file located at above "path_to_file".


            HINT: remove "pass", it's a keyword that is not needed.
            HINT: request comes back as json.
            HINT: test_trivia_handler.py will assist you in this challenge, look at the "expected_response"
            strings.
            HINT: It may be necessary to cast objects.
            HINT: there is also a fully functional bot that you can use to see how the game works.

            :return: a trivia question.
        """
        r = requests.get('http://jservice.io/api/random')
        j = json.loads(r.text)
        category = str(j[0]['category']['title'])
        question = str(j[0]['question'])
        answer = str(j[0]['answer'])

        response_question = {'text': '>*Category: %s*\n\n>*Question: %s*' % (category, question)}
        response_answer = {'text': '>*Answer: %s*' % answer}
        self.store_trivia_answer(response_answer, path_to_file)

        return str(response_question['text'])

    def get_trivia_answer(self, path_to_file="data_files/trivia_answer.json"):
        answer = ''
        if not os.path.isfile(path_to_file):
            return '**No Question**<br>Use \"trivia_question\" to get a new question.'

        with open(path_to_file) as json_file:
            answer = json.load(json_file)

        os.remove(path_to_file)
        return str(answer['text'])

    def store_trivia_answer(self, response_answer, path_to_file):
        with open(path_to_file, 'w') as json_file:
            json.dump(response_answer, json_file)

