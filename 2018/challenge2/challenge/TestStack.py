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
        It is used to verify that a part of your code
        is correct, and retruning the values you expect.
        '''
        assert 2 == 2

        temp_var = "Hello World"
        assert "Hello World" is temp_var


    def test_001_check_stack_is_empty(self):
        '''
            Finish the assert to check if the
            stack is empty.
        '''


    def test_102_check_stack_not_empty(self):
        '''
            Finish the assert to check if the
            stack is not empty.
        '''
        for i in range(1, 5):
            self.jam_stack.push("item {}".format(i))



    def test_103_check_adding_two_items(self):
        '''
            Finish the test by adding item_one and
            item_two to the stack and then checking
            if the stack has a size of two.
        '''
        item_one = "item 1"
        item_two = "item 2"


    def test_104_peek_at_top_element(self):
        '''
            Finish the test by adding item_one and
            item_two to the stack and then checking
            the stacks last item is item_two.
        '''
        item_one = "item 1"
        item_two = "item 2"



    def test_105_check_pop_items(self):
        '''
            Finish the test by popping
            one item from the stack,
            checking the size is one.
            Popping another item and
            lastly checking if the stack
            is empty.
        '''
        for i in range(1, 3):
            self.jam_stack.push("item {}".format(i))

        assert self.jam_stack.size() == 2

    def test_106_check_peek(self):
        '''
            Finish the asset to check if peek
            is looking at the correct item.
        '''
        for i in range(1, 6):
            self.jam_stack.push("item {}".format(i))


    def test_107_check_max_size(self):
        '''
            Finish the test by assert that
            the stack is the size of
            the MAX_STACK_SIZE.
            Then try to push another_item.
            Finally assert that the stack is
        '''
        for i in range(1, self.jam_stack.get_max_size() + 1):
            self.jam_stack.push("item {}".format(i))


    @classmethod
    def tearDownClass(cls):
        super(TestStack, cls).tearDownClass()

    def tearDown(self):
        super(TestStack, self).tearDown()
        self.jam_stack = None


if __name__ == '__main__':
    unittest.main()
