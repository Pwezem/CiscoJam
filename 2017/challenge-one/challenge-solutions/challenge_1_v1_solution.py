class CiscoJamChallengeOne:


    stringToBeReversed = 'you_need_to_reverse_this_string'
    unorderedList = ['Hello', 'World', 'Cisco', 'Jam' , 'Spark', 'Bot', 'Challenge',
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
        print palindromes

    # Write the method that will reverse a string passed in as a parameter.
    def taskOne(stringToBeReversed):
    	originalString = stringToBeReversed
    	reversedString = ""
    	stringLen      = len(originalString)
        
    	for counter in range(stringLen, 0, -1):
    		reversedString = reversedString + originalString[counter]

    	return reversedString

    # Complete the method to sort a list of words into alphabetical order.
    def taskTwo():


    def taskThree():
    	


if __name__ == '__main__':
    main()