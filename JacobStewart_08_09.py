# Jacob L Stewart
# Chapter 8 Assignment 09
# Program that requests two strings and prints:
# characters that occur in both strings
# characters that occur in one string and not the other
# letters that don't occur in either string.

def main():
    # setting alphabet to find what letters don't occur in strings.
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    allLetters = set(alphabet)

    # get user input for 2 strings
    firstString = input("Enter your first string: ")
    secondString = input("Enter your second string: ")

    # transforming input into sets
    set1 = set(firstString)
    set2 = set(secondString)

    # finds the union or list of all letters in both strings
    print("Characters that occur in both strings: " + str(set1.union(set2)))
    # finds the difference of first string from second string
    print("Characters that occur in first input and not the second: " + str(set1.difference(set2)))
    # finds the difference of second string from first string
    print("Characters that occur in second input and not the first: " + str(set2.difference(set1)))
    # compares the union of both strings and gets the difference from the predefined alphabet.
    print("Characters that dont occur in either input: " + str(allLetters.difference(str(set1.union(set2)))))


main()
