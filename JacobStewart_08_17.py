# Jacob L Stewart
# Chapter 8 Assignment 17
# Write a program that reads 5 states and capitals into a dictionary whose keys are state names and
# whose values are the capital. Then the program should prompt the user to enter state names and
# print the corresponding values. Stop when the user enters quit.

def main():
    # checks whether a file should be used
    useFile = input("Would you like to use a file? Y/N \n(Format should follow State;Capital for each line): ")
    if useFile.upper() == "Y":
        state_capital = getStates(input("Enter file name: "))
    else:
        # assigns 5 states and capitals into dictionary @ state_capital
        state_capital = {"FLORIDA": "Tallahassee", "TEXAS": "Austin", "CALIFORNIA": "Sacramento",
                         "ALASKA": "Juneau", "ARIZONA": "Phoenix"}
    # getting the state name
    state = input('Enter state name: ')
    # upper to prevent case errors
    state = state.upper()
    # while quit isn't entered continue.
    while state != "QUIT":
        # checking if input is in list of states
        if state in state_capital:
            # prints value of state in dictionary
            print("Capital of " + state + " is " + state_capital[state])
            # re prompts user and converts input to upper
            state = input('Enter state name: ')
            state = state.upper()
        else:
            print(state, 'does not exist in dictionary, states loaded are:')
            # initialize states
            states = ""
            # gets all state names in dictionary and displays to user
            for x in state_capital:
                states = states + x + " "
            print(states)
            # re prompts user and converts input to upper
            state = input('Enter state name: ')
            state = state.upper()


def getStates(filename):
    fileExists(filename)
    states = open(filename, "r")
    # map to attach capitals to states
    state_capital = {}
    for line in states:
        # creates array of fields using ; to split the data
        fields = line.split(";")
        stateName = fields[0].upper()
        if stateName not in state_capital:
            state_capital[stateName] = ""
        state_capital[stateName] += fields[1]
    # closing file
    states.close()
    return state_capital


def fileExists(text):
    try:
        # forces file open and attempts to read it.
        with open(text) as fileObject:
            fileObject.read()
    except FileNotFoundError:
        print("File", text, "not found!")
        exit()


main()

# FILE EXAMPLE
# florida;Tallahassee
# california;Sacramento
