import logging as log
import os.path
import unittest

from utils.logging_utils import Utils


class testJeoprady(unittest.TestCase):
    score = 0

    @classmethod
    def setUpClass(cls):
        super(testJeoprady, cls).setUpClass()
        log.getLogger("testTrivia")
        cls.utils = Utils()

    def test_100_trivia_question_returned(self):
        """
            Simple test to check if Trivia works and returns a question json blob.
        """
        log.info("Starting Test 100 trivia question returned")

        response = self.numbers.handle_message('triviaquestion')

        expected_response = {'text': 'This is a sample question'}

        self.assertIsNotNone(response, "ERROR, returned question is none.")

        self.assertEqual(type(response), type(expected_response),
                         "ERROR, received incorrect response data type. Expected %s, received %s"
                         % (type(response), type(expected_response)))

        log.info("Finished Test 100")

    def test_101_trivia_answer_returned(self):
        """
            Simple test to check if Trivia works and returns an appropriate answer,
            and that a file to store the answer is generated
        """
        log.info("Starting Test 101 trivia answer returned")
        
        expected_response = {'text': 'This is a sample answer'}

        # Generate answer file to test with
        with open('handlers/data_files/trivia_answer.json') as json_file:
            answer = json.load(expected_response)

        response = self.numbers.handle_message('triviaanswer')


        self.assertEqual(type(response), type(expected_response),
                         "ERROR, received incorrect response data type. Expected %s, received %s"
                         % (type(response), type(expected_response)))

        self.assertEqual(response, expected_response, "ERROR. Expected answer does not match response")

        self.assertNotEqual(response, 'No Question',
                         "ERROR, could not find answer - no question file found"
                         % (response, expected_response))

        log.info("Finished Test 101")

    def test_102_trivia_answer_file_deleted_after_answer_given(self):
        """
            Simple test to check check if the Trivia answer file is deleted once the answer is given
        """
        log.info("Starting Test 102 trivia answer file deleted after answer given")

        # Generate answer file to test with
        with open('handlers/data_files/trivia_answer.json') as json_file:
            answer = json.load(expected_response)

        self.numbers.handle_message(self.numbers.handle_message('triviaanswer'))

        does_file_exist = os.path.isfile('handlers/data_files/trivia_answer.json')

        self.assertEqual(does_file_exist, False,
                         "ERROR, answer file was not deleted after the answer was given")

        log.info("Finished Test 102")

if __name__ == '__main__':
    unittest.main()
