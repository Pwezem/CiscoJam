"""
Welcome to Challege One!
Please follow the instructions in the docstrings of each Task method.
"""

stringToBeReversed = 'you_need_to_reverse_this_string'
unorderedList = ['Hello', 'World', 'Cisco', 'Jam' , 'Spark', 'Bot', 'Challenge',
                 'Put', 'This', 'List', 'In', 'Alphabetical', 'Order']
possible_palindromes = ["M3o2m", "N4au5ruan9", "12Hag3ig5ah", "Ai5bohp8hobia", "Ta89cocat", "7Racecar09", "Suc90cus",
               "Pip8pip", "Civ34ic9", "Ma8ma", "Kay8ak", "0I2g3ig54i", "Deta8rtrated"]

def main():
    reversedString = taskOne_reverse_string(stringToBeReversed)
    print "Task 1: Printing Reversed String: " + reversedString

    sortedList = taskTwo_sort_list(unorderedList)
    print "Task 2: Printing Sorted List: " + str(sortedList)

    sortedFilteredPalindromes = taskThree_filter_palindromes(possible_palindromes)
    print "Task 3: Printing Filtered Palindromes: " + str(sortedFilteredPalindromes)

def taskOne_reverse_string(stringToBeReversed):
    """
    Write a method that will reverse a string passed in as a parameter,
    and return it.
    """
    
    # TODO

    return reversedString

# Complete the method to sort a list of words into alphabetical order.
def taskTwo_sort_list(unorderedList):
    """
    Write a method that will sort a list of words into alphabetical order,
    and returns the list.
    Hint: Use your sorting algorithm knowledge.
    No points for using .sorted()
    """
    
    # TODO

    return unorderedList

def taskThree_filter_palindromes(possible_palindromes):
    """
    Write a method that removes the numbers from the strings
    in the method parameter list. Filter which of the strings
    are palindromes.
    HINT: Use your solution from Task One to check for Palindromes
    """

    # TODO

    return palindromes

if __name__ == '__main__':
    main()