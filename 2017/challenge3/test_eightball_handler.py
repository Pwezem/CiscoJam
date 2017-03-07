import unittest
import logging as log
from utils.logging_utils import Utils
from sparkBot.handlers.eightball import Eightball


class testEightball(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(testEightball, cls).setUpClass()
        log.getLogger("testFuturama")
        with open("test_logs/eightball_test.log", 'w') as test_file:
            test_file.truncate()
        log.basicConfig(filename='test_logs/eightball_test.log', level=log.DEBUG,
                        format='[%(asctime)s]:%(levelname)s: %(message)s')
        cls.utils = Utils()

    def setUp(self):
        super(testEightball, self).setUp()
        self.eightball = Eightball("sparkBot/lhandlers/data_files/eightball.json")

    def test_100_futurama_quote(self):
        """
            Simple test to check futurama works and returns a quote.
        """
        self.utils.banner("Starting Test 100 futurama command")

        response = self.eightball.handle_message("{}".format("eightball"),
                                                 "test_email@email.mail",
                                                 username="Testa")

        self.assertTrue(response in self.eightball.data["predictions"],
                        "ERROR, response \"%s\" was not in the list of predictions."
                        % response)

        self.utils.end_banner("Finished Test 100")

    @classmethod
    def tearDownClass(cls):
        super(testEightball, cls).tearDownClass()

    def tearDown(self):
        super(testEightball, self).tearDownClass()
        self.futurama = None

if __name__ == '__main__':
    unittest.main()
