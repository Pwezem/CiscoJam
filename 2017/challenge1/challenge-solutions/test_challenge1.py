import unittest

import challenge1 as challenge1


class testChallenge1(unittest.TestCase):
    score = 0
    
    @classmethod
    def setUpClass(cls):
        super(testChallenge1, cls).setUpClass()

    def setUp(self):
        super(testChallenge1, self).setUp()
        self.reversed_string = "gnirts_siht_esrever_ot_deen_uoy"
        self.palindromes = ['Mom', 'Nauruan', 'Hagigah', 'Aibohphobia',
                   'Tacocat', 'Racecar', 'Succus', 'Pippip', 'Civic',
                   'Kayak', 'Igigi', 'Detartrated']
        self.sorted_list = ['Alphabetical', 'Bot', 'Challenge', 'Cisco', 'Hello',
               'In', 'Jam', 'List', 'Order', 'Put', 'Spark', 'This', 'World']

    def test_100_task_one_reverse_a_string(self):
        """
            Simple test to check task one works and returns a correct stuff.
        """
        response = challenge1.taskOne_reverse_string(challenge1.stringToBeReversed)

        self.assertEqual(self.reversed_string, response,
                         "ERROR, response \"%s\" did not match expected \"%s\"."
                         % (response, self.reversed_string))

        self.__class__.score += 10

    def test_101_task_two_sort_a_list(self):
        """
            Simple test to check task two works and returns a correct stuff.
        """
        response = challenge1.taskTwo_sort_list(challenge1.unorderedList)

        self.assertEqual(self.sorted_list, response,
                         "ERROR, Lists were not sorted correctly, response \"%s\" did not match expected \"%s\"."
                         % (response, self.sorted_list))

        self.__class__.score += 15

    def test_102_task_three_palindrome(self):
        """
            Simple test to check task three works and returns a correct stuff.
        """
        response = challenge1.taskThree_filter_palindromes(challenge1.possible_palindromes)

        self.assertEqual(self.palindromes, response,
                         "ERROR, Lists were not sorted correctly, response \"%s\" did not match expected \"%s\"."
                         % (response, self.palindromes))

        self.__class__.score += 25

    def is_palindrome(self, string):
        string = string.lower()
        for i, char in enumerate(string):
            if char != string[-i - 1]:
                return False
        return True

    @classmethod
    def tearDownClass(cls):
        super(testChallenge1, cls).tearDownClass()
        print("\n\n*******************************")
        print("Score for tests \"%d/50\"" % cls.score)
        print("*******************************")

    def tearDown(self):
        super(testChallenge1, self).tearDownClass()
        self.futurama = None

if __name__ == '__main__':
    unittest.main()
