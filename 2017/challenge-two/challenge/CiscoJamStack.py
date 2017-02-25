# Maximum number of items the stack can hold.
MAX_STACK_SIZE = 10

"""
    Your Challenge is to fix and/or write the code below, each method comes with a description
    of how the method works, what it does and what it returns.

"""

class CiscoJamStack:

    def __init__(self, max_size=10):
        '''
        Constructor, creates a stack.
        Called by a = Stack().
        '''
        self.MAX_STACK_SIZE = max_size
        self.items = []

    def isEmpty(self):
        '''
        Checks if the stack is empty.
        Should retrun true or false if there are
        no items in the stack.
        :return: boolean
        '''


    def push(self, item):
        '''
        Adds an item to the stack.
        First checks that the maximum limit of
        the stack has not been reached.
        If the maximum is not reached, add the
        item to the stack.
        :param item: item to push to stack.
        :return: boolean, true if item was added
                 false if item was not added.
        '''
        if self.size() < MAX_STACK_SIZE:



    def pop(self):
        '''
        Pops the next item off the stack.
        Should check if the satck is empty first.
        :return: Returns the top item on the
                 stack. Returns false if no
                 item can be popped.
        '''

    def size(self):
        '''
        Returns the size of the stack.
        :return: size of stack.
        '''
        return

    def peek(self):
        '''
        look at the top item on the stack.
        :return: the top item on the stack
                 unpopped.
        '''
        return self.items[self.size() - 1]

    def get_max_size(self):
        '''
        Returns the maximum size of the stack.
        :return: Returns a max int.
        '''
        return MAX_STACK_SIZE
