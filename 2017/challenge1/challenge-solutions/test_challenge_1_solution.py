import unittest
import logging as log
import challenge_1_v1_solution as challenge1


class testChallenge1(unittest.TestCase):
    score = 0

    @classmethod
    def setUpClass(cls):
        super(testChallenge1, cls).setUpClass()

    def setUp(self):
        super(testChallenge1, self).setUp()

    def test_100_task_one_reverse_a_string(self):
        """
            Simple test to check task one works and returns a correct stuff.
        """
        expected_output = challenge1.stringToBeReversed[::-1]
        response = challenge1.taskOne_reverse_string(challenge1.stringToBeReversed)

        self.assertEqual(response, expected_output,
                         "ERROR, response \"%s\" did not match expected \"%s\"."
                         % (response, expected_output))

        self.__class__.score += 5

    def test_101_task_two_sort_a_list(self):
        """
            Simple test to check task two works and returns a correct stuff.
        """
        expected_output = sorted(challenge1.unorderedList)
        response = challenge1.taskTwo_sort_list(challenge1.unorderedList)

        self.assertEqual(response, expected_output,
                         "ERROR, Lists were not sorted correctly, response \"%s\" did not match expected \"%s\"."
                         % (response, expected_output))

        self.__class__.score += 10

    def test_102_task_three_palindrome(self):
        """
            Simple test to check task three works and returns a correct stuff.
        """
        palindromes = challenge1.possible_palindromes
        output = []
        for string in palindromes:
            output.append(''.join([i for i in string if not i.isdigit()]))

        expected_output = []
        for string in output:
            if self.is_palindrome(string):
                expected_output.append(string)

        response = challenge1.taskThree_filter_palindromes(challenge1.possible_palindromes)

        self.assertEqual(response, expected_output,
                         "ERROR, Lists were not sorted correctly, response \"%s\" did not match expected \"%s\"."
                         % (response, expected_output))

        self.__class__.score += 15

    def is_palindrome(self, string):
        string = string.lower()
        for i, char in enumerate(string):
            if char != string[-i - 1]:
                return False
        return True

    @classmethod
    def tearDownClass(cls):
        super(testChallenge1, cls).tearDownClass()
        print "\n\n*******************************"
        print "Score for tests \"%d/30\"" % cls.score
        print "*******************************"

    def tearDown(self):
        super(testChallenge1, self).tearDownClass()
        self.futurama = None

if __name__ == '__main__':
    unittest.main()
