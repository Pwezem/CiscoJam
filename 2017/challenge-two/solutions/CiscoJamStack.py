# Maximum number of items the stack can hold.
MAX_STACK_SIZE = 10


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
        :return: boolean
        '''
        if not self.items:
            return True
        else:
            return False

    def push(self, item):
        '''
        Add an item to the stack.
        Checks that the max limit of
        the stack has not been reached.
        :param item: item to push to stack.
        :return: boolean, true if item was added
                 false if item was not added.
        '''
        if self.size() < MAX_STACK_SIZE:
            self.items.append(item)
            return True
        else:
            return False

    def pop(self):
        '''
        Pops the next item off the stack.
        :return: Returns the top item on the
                 stack. Returns false if no
                 item can be popped.
        '''
        if not self.isEmpty():
            #return self.items.pop() <-- simple way, another would be with a counter.
            item = self.items[self.size() - 1]
            self.items.remove(item)
            return item
        return False

    def peek(self):
        '''
        look at the top item on the stack.
        :return: the top item on the stack
                 unpopped.
        '''
        return self.items[self.size() - 1]

    def size(self):
        '''
        Returns the size of the stack.
        :return: size of stack.
        '''
        return len(self.items)

    def get_max_size(self):
        '''
        Returns the maximum size of the stack.
        :return: Returns a max int.
        '''
        return MAX_STACK_SIZE
