import unittest
import logging as log
from utils.logging_utils import Utils
from sparkBot.handlers.numbers import Numbers


class testNumbers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(testNumbers, cls).setUpClass()
        log.getLogger("testFuturama")
        with open("test_logs/futurama_test.log", 'w') as test_file:
            test_file.truncate()
        log.basicConfig(filename='test_logs/futurama_test.log', level=log.DEBUG,
                        format='[%(asctime)s]:%(levelname)s: %(message)s')
        cls.utils = Utils()

    def setUp(self):
        super(testNumbers, self).setUp()
        self.numbers = Numbers()

    def test_100_numbers_quote(self):
        """
            Simple test to check numbers works and returns a no game due to no options supplied.
        """
        self.utils.banner("Starting Test 100 numbers command")

        response = self.numbers.handle_message("{}".format("numbers"), "test_email@email.mail",
                                               username="Testa")

        self.assertTrue(response in self.futurama.quotes,
                        "ERROR, response \"%s\" was not in the."
                        % response)

        self.utils.end_banner("Finished Test 100")

    @classmethod
    def tearDownClass(cls):
        super(testNumbers, cls).tearDownClass()

    def tearDown(self):
        super(testNumbers, self).tearDownClass()
        self.futurama = None

if __name__ == '__main__':
    unittest.main()
