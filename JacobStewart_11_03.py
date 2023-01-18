# Jacob L Stewart
# Chapter 11 Assignment 03
# Write a recursive function reverse(text) that reverses a string.
# For example, reverse("Hello!") returns the string "!olleH".
# Implement a recursive solution by removing the first character,
# reversing the remaining text, and combining the two.

def reverse(text):
    if len(text) == 0:
        return text
    else:
        return reverse(text[1:]) + text[0]


def main():
    text = input("Enter your text: ")
    print("Reverse of what you wrote: ", reverse(text))


main()
