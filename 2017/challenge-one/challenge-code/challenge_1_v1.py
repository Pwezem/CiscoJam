stringToBeReversed = 'you_need_to_reverse_this_string'
unorderedList = ['Hello', 'World', 'Cisco', 'Jam', 'Spark', 'Bot', 'Challenge',
                 'Put', 'This', 'List', 'In', 'Alphabetical', 'Order']
palindromes = ["M3o2m", "N4au5ruan9", "12Hag3ig5ah", "Ai5bohp8hobia", "Ta89cocat", "7Racecar09", "Suc90cus",
               "Pip8pip", "Civ34ic9", "Ma8ma", "Kay8ak", "0I2g3ig54i", "Deta8rtrated"]


def main():
    reversedString = taskOne(stringToBeReversed)
    print "Printing Reversed String: " + reversedString

    sortedList = taskTwo(unorderedList)
    print "Printing Sorted List: "
    print sortedList

    sortedFilteredPalindromes = taskThree(palindromes)
    print "Printing Filtered Palindromes: "
    print sortedFilteredPalindromes


# Write the method that will reverse a string passed in as a parameter.
def taskOne(stringToBeReversed):
    originalString = stringToBeReversed
    reversedString = ""
    stringLen = len(originalString)

    for counter in range(stringLen-1, 0, -1):
        reversedString = reversedString + originalString[counter]

    return reversedString


# Complete the method to sort a list of words into alphabetical order.
def taskTwo(word_list):
    print word_list
    def swap(input_list, word_a, word_b):
        index_a = input_list.index(word_a)
        index_b = input_list.index(word_b)

        #word_list = word_list
        input_list.remove(word_a)
        input_list.insert(index_a, word_b)
        input_list.remove(word_b)
        input_list.insert(index_b, word_a)

        return input_list

    for i in xrange(len(word_list)-1):
        word = word_list[i]
        next_word = word_list[i+1]
        if word[0] > next_word[0]:
            word_list = swap(word_list, word, next_word)

    print word_list

def taskThree(palindromes):
    pass

if __name__ == '__main__':
    main()