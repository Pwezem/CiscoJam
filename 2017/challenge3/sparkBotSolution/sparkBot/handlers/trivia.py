import os
import requests
from handler_base import MessageHandler
import json

class Trivia(MessageHandler):

    def __init__(self, path_to_file="handlers/data_files/trivia_answer.json"):
        # Store the path_to_file for later use.
        self.answer_file = path_to_file
        with open(self.answer_file) as json_file:
            self.answer = (json.load(json_file))["text"]

    def handle_message(self, raw_msg, user_email, username):
        if "trivia question" in str(raw_msg).lower():
            return self.get_trivia_question()
        if "trivia answer" in str(raw_msg).lower():
            return self.get_trivia_answer()
        return False

    def help(self):
        return "**Trivia** - Returns a randomly pulled jeoprady question"

    def get_trivia_question(self):
        if self.answer:
            return "**Trivia insession**<br>Please get the answer to the last question"
        r = requests.get('http://jservice.io/api/random')
        j = json.loads(r.text)
        category = j[0]["category"]["title"]
        question = j[0]["question"]
        self.answer = ">*Answer: %s*" % j[0]["answer"]

        response_question = ">*Category: %s*<br><br>>*Question: %s*" % (category, question)
        self.store_trivia_answer({"text": self.answer})

        return response_question

    def get_trivia_answer(self):
        if not self.answer:
            return "**No Question**<br>Use \"trivia question\" to get a new question."

        ans = self.answer
        self.answer = ""

        self.store_trivia_answer({"text": self.answer})

        return ans

    def store_trivia_answer(self, response_answer):
        with open(self.answer_file, 'w') as json_file:
            json.dump(response_answer, json_file)

