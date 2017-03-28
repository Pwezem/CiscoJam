import os
import requests
from handler_base import MessageHandler
import json

class Trivia(MessageHandler):

    def __init__(self, path_to_file="handlers/data_files/trivia_answer.json"):
        # Store the path_to_file for later use.
        self.answer_file = path_to_file

    def handle_message(self, raw_msg, user_email, username):
        if "trivia question" in str(raw_msg).lower():
            return self.get_trivia_question()
        if "trivia answer" in str(raw_msg).lower():
            return self.get_trivia_answer()
        return False

    def help(self):
        return "**Trivia** - Returns a randomly pulled jeoprady question"

    def get_trivia_question(self):
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

    def get_trivia_answer(self):
        """
            This method should return the answer to the last question asked.
            If no answer exists a question wasn't asked and therefore
            this should be returned "**No Question**<br>Use \"trivia question\" to get a new question."


            HINT: remove "pass", it's a keyword that is not needed.
            HINT: check json file exists.
            HINT: Return the answer if it's there.
            HINT: test_trivia_handler.py will assist you in this challenge, look at the "expected_response"
            strings.
            HINT: It may be necessary to cast objects.
            HINT: there is also a fully functional bot that you can use to see how the game works.

            :return: a trivia answer or a string with no question.
        """
        pass

    def store_trivia_answer(self, response_answer):
        with open(self.answer_file, 'w') as json_file:
            json.dump(response_answer, json_file)

