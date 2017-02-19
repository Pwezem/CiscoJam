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

# Write the method that will reverse a string passed in as a parameter.
def taskOne_reverse_string(stringToBeReversed):
    originalString = stringToBeReversed
    reversedString = ""
    stringLen      = len(originalString)

    for counter in range(stringLen - 1, -1, -1):
        reversedString = reversedString + originalString[counter]

    return reversedString

# Complete the method to sort a list of words into alphabetical order.
def taskTwo_sort_list(unorderedList):
    for word_index in range(len(unorderedList) - 1, 0, -1):
        for i in range(word_index):
            if unorderedList[i] > unorderedList[i+1]:
                temp = unorderedList[i]
                unorderedList[i] = unorderedList[i+1]
                unorderedList[i+1] = temp

    return unorderedList

def taskThree_filter_palindromes(possible_palindromes):
    removed_numbers = []
    palindromes = []

    for word in possible_palindromes:
        word_without_numbers = ''

        for char in range(len(word)):
            if word[char].isalpha():
                word_without_numbers = word_without_numbers + word[char]

        removed_numbers.append(word_without_numbers)
            
    for word in removed_numbers:
        if word.lower() == taskOne_reverse_string(word).lower():
            palindromes.append(word)

    return palindromes

if __name__ == '__main__':
    main()