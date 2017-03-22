import logging as log
import unittest

from sparkBot.handlers.eightball import Eightball
from utils.logging_utils import Utils


class testEightball(unittest.TestCase):
    score = 0

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
        self.eightball = Eightball("sparkBot/handlers/data_files/eightball.json")

    def test_100_eightball_prediction(self):
        """
            Simple test to check eightball works and returns a prediction.
        """
        self.utils.banner("Starting Test 100 eightball command")

        response = self.eightball.handle_message("{}".format("eightball"),
                                                 "test_email@email.mail",
                                                 username="Testa")
        self.__class__.score += 5

        self.assertTrue(response in self.eightball.data["predictions"],
                        "ERROR, response \"%s\" was not in the list of predictions."
                        % response)

        self.__class__.score += 10
        self.utils.end_banner("Finished Test 100")

    @classmethod
    def tearDownClass(cls):
        super(testEightball, cls).tearDownClass()
        print "\n\n*******************************"
        print "Score for tests \"%d/15\"" % cls.score
        print "*******************************"

    def tearDown(self):
        super(testEightball, self).tearDownClass()
        self.futurama = None

if __name__ == '__main__':
    unittest.main()
