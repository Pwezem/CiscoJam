import logging as log
import os.path
import unittest
import json
import re

from sparkBot.handlers.trivia import Trivia
from utils.logging_utils import Utils


class testTrivia(unittest.TestCase):
    score = 0

    @classmethod
    def setUpClass(cls):
        super(testTrivia, cls).setUpClass()
        log.getLogger("testTrivia")
        cls.question_pattern = ">\*Category: .*<br><br>>\*Question: .*\*"
        with open("test_logs/eightball_test.log", 'w') as test_file:
            test_file.truncate()
        log.basicConfig(filename='test_logs/trivia_test.log', level=log.DEBUG,
                        format='[%(asctime)s]:%(levelname)s: %(message)s')
        cls.path_to_file = "testing_files/trivia_test.json"
        cls.utils = Utils()

    def setUp(self):
        super(testTrivia, self).setUp()
        self.trivia = Trivia(path_to_file=self.path_to_file)

    def test_100_trivia_question_returned(self):
        """
            Simple test to check if Trivia works and returns a question json blob.
        """
        log.info("Starting Test 100 trivia question returned")

        response = self.trivia.handle_message('trivia question', user_email="test_email@email.mail",
                                              username="Testa")

        pattern = re.compile(self.question_pattern)

        self.assertIsNotNone(response, "ERROR, returned question is none.")

        self.assertTrue(pattern.match(response),
                        "ERROR, received incorrect response data type. Response was %s,"
                        "expect to match pattern %s"
                        % (response, self.question_pattern))

        log.info("Finished Test 100")

    def test_101_trivia_answer_returned(self):
        """
            Simple test to check if Trivia works and returns an appropriate answer,
            and that a file to store the answer is generated
        """
        log.info("Starting Test 101 trivia answer returned")

        # Generate answer file to test with
        with open(self.path_to_file) as json_file:
            expected_response = json.load(json_file)

        response = self.trivia.handle_message('trivia answer', user_email="test_email@email.mail",
                                              username="Testa")


        self.assertEqual(response, expected_response["text"],
                         "ERROR, received incorrect response data type. Expected %s, received %s"
                         % (response, expected_response))

        # self.assertNotEqual(response, 'No Question',
        #                  "ERROR, could not find answer - no question file found"
        #                  % (response, expected_response))

        log.info("Finished Test 101")

    def _test_102_trivia_answer_file_deleted_after_answer_given(self):
        """
            Simple test to check check if the Trivia answer file is deleted once the answer is given
        """
        log.info("Starting Test 102 trivia answer file deleted after answer given")

        # Generate answer file to test with
        with open('handlers/data_files/trivia_answer.json') as json_file:
            expected_response = json.load(json_file)

        self.trivia.handle_message("trivia answer")

        does_file_exist = os.path.isfile('handlers/data_files/trivia_answer.json')

        self.assertEqual(does_file_exist, False,
                         "ERROR, answer file was not deleted after the answer was given")

        log.info("Finished Test 102")

    @classmethod
    def tearDownClass(cls):
        super(testTrivia, cls).tearDownClass()
        print "\n\n*******************************"
        print "Score for tests \"%d/25\"" % cls.score
        print "*******************************"

    def tearDown(self):
        super(testTrivia, self).tearDownClass()
        self.futurama = None

if __name__ == '__main__':
    unittest.main()
