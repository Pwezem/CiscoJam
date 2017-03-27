import json
import os
import unittest

from sparkBot.handlers.trivia import Trivia

from utils.logging_utils import Utils


class testTrivia(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(testTrivia, cls).setUpClass()
        cls.utils = Utils()

    def setUp(self):
        super(testTrivia, self).setUp()
        self.trivia = Trivia()

    def tearDown(self):
        if os.path.isfile('sparkBot/handlers/data_files/trivia_answer.json'):
            os.remove('sparkBot/handlers/data_files/trivia_answer.json')

    def test_100_trivia_question_returned(self):
        """
            Simple test to check if Trivia works and returns a question json blob.
        """
        self.utils.log("Starting Test 100 trivia question returned")

        response = self.trivia.handle_message('trivia_question', "test_email@email.mail",
                                              username="Testa")

        expected_response = {'text': 'This is a sample question'}

        self.assertIsNotNone(response, "ERROR, returned question is none.")

        self.assertEqual(type(response), type(expected_response['text']),
                         "ERROR, received incorrect response data type. Received %s, Expected %s"
                         % (type(response), type(expected_response['text'])))

        self.utils.log("Finished Test 100")

    def test_101_trivia_answer_returned(self):
        """
            Simple test to check if Trivia works and returns an appropriate answer type
        """
        self.utils.log("Starting Test 101 trivia answer returned")
        
        expected_response = {'text': 'This is a sample answer'}
        
        self.trivia.handle_message('trivia_question', 'test_email@email.mail',
                                   username='Testa')

        response = self.trivia.handle_message('trivia_answer', "test_email@email.mail",
                                              username="Testa")

        self.assertEqual(type(response), type(expected_response['text']),
                         "ERROR, received unexpected response. Received %s, Expected %s"
                         % (type(response), type(expected_response['text'])))

        self.assertNotEqual(str(response), 'No Question',
                            'ERROR, could not find answer - no question file found')

        self.utils.log("Finished Test 101")

    def test_102_trivia_answer_file_deleted_after_answer_given(self):
        """
            Simple test to check check if the Trivia answer file is deleted once the answer is given
        """
        self.utils.log("Starting Test 102 trivia answer file deleted after answer given")
        
        expected_response = {'text': 'This is a sample answer'}

        # Generate answer file to test with
        with open('sparkBot/handlers/data_files/trivia_answer.json', 'w') as json_file:
            json.dump(expected_response, json_file)

        self.trivia.handle_message('trivia_answer', "test_email@email.mail",                                                username="Testa")

        does_file_exist = os.path.isfile('sparkBot/handlers/data_files/trivia_answer.json')

        self.assertEqual(does_file_exist, False,
                         "ERROR, answer file was not deleted after the answer was given")

        self.utils.log("Finished Test 102")

if __name__ == '__main__':
    unittest.main()
