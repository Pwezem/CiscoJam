import unittest

from CiscoJamStack import CiscoJamStack as jam_stack


class TestStack(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestStack, cls).setUpClass()

    def setUp(self):
        super(TestStack, self).setUp()
        self.jam_stack = jam_stack()

    def test_000_example_test_case(self):
        '''
        assert is the important keyword.
        It is used to verify that a part of your test
        is correct.
        '''
        assert 2 == 2

    def test_001_check_stack_is_empty(self):
        assert self.jam_stack.isEmpty()

    def test_102_check_stack_not_empty(self):
        for i in range(1, 5):
            self.jam_stack.push("item {}".format(i))

        assert not self.jam_stack.isEmpty()

    def test_103_check_adding_two_items(self):
        for i in range(1, 3):
            self.jam_stack.push("item %d" % i)

        assert self.jam_stack.size() == 2

    def test_104_peek_at_top_element(self):
        item_one = "item 1"
        item_two = "item 2"

        self.jam_stack.push(item_one)
        self.jam_stack.push(item_two)

        assert item_two is self.jam_stack.peek()

    def test_105_check_pop_items(self):
        for i in range(1, 3):
            self.jam_stack.push("item {}".format(i))

        assert self.jam_stack.size() == 2

        item_two = self.jam_stack.pop()

        assert self.jam_stack.size() == 1

        item_two = self.jam_stack.pop()

        assert self.jam_stack.isEmpty()

    def test_106_check_max_size(self):
        for i in range(1, self.jam_stack.get_max_size() + 1):
            self.jam_stack.push("item {}".format(i))

        assert self.jam_stack.size() == self.jam_stack.get_max_size()

        self.jam_stack.push("Should not be added")

        assert self.jam_stack.size() == self.jam_stack.get_max_size()

    @classmethod
    def tearDownClass(cls):
        super(TestStack, cls).tearDownClass()

    def tearDown(self):
        super(TestStack, self).tearDown()
        self.jam_stack = None


if __name__ == '__main__':
    unittest.main()
