import logging as log
import unittest

from sparkBot.handlers.meaningoflife import MeaningOfLife

from utils.logging_utils import Utils


class testMeaningOfLife(unittest.TestCase):
    score = 0

    @classmethod
    def setUpClass(cls):
        super(testMeaningOfLife, cls).setUpClass()
        log.getLogger("testFuturama")
        with open("test_logs/futurama_test.log", 'w') as test_file:
            test_file.truncate()
        log.basicConfig(filename='test_logs/futurama_test.log', level=log.DEBUG,
                        format='[%(asctime)s]:%(levelname)s: %(message)s')
        cls.utils = Utils()

    def setUp(self):
        super(testMeaningOfLife, self).setUp()
        self.meaningoflife = MeaningOfLife()

    def test_100_meaning_of_life(self):
        """
            Simple test to check meaning of life works and returns 42.
        """
        self.utils.banner("Starting Test 100 meaning of life command")

        response = self.meaningoflife.handle_message("{}".format("meaning of life"),
                                                     "test_email@email.mail",
                                                     username="Testa")

        expected = "42 Testa"
        self.assertEquals(response, expected,
                          "ERROR, response \"%s\" was not the same as expected response %s."
                          % (response, expected))

        self.utils.end_banner("Finished Test 100")
        self.__class__.score += 5

    @classmethod
    def tearDownClass(cls):
        super(testMeaningOfLife, cls).tearDownClass()
        print "\n\n*******************************"
        print "Score for tests \"%d/5\"" % cls.score
        print "*******************************"

    def tearDown(self):
        super(testMeaningOfLife, self).tearDownClass()
        self.meaningoflife = None


if __name__ == '__main__':
    unittest.main()
