# Jacob L Stewart
# Chapter 7 Assignment 01
# Writes Hello, World! to a file then opens and prints the file to console.

def main():
    # calls function and prints "Hello, World!"
    writeFile("Hello, World!")
    readFile()


# @param text to store whatever message needed.
# opens file hello.txt writes @text and closes file.
def writeFile(text):
    writeHelloWorld = open("../hello.txt", "w")
    writeHelloWorld.write(text)
    writeHelloWorld.close()


# opens file hello.txt and prints text. closes file.
def readFile():
    readHelloWorld = open("../hello.txt", "r")
    line = readHelloWorld.readline()
    print(line)
    readHelloWorld.close()


# calls main function
main()
