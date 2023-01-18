# Jacob L Stewart
# Chapter 5 Assignment 30
# Prompts user to create a password and validates based on following parameters:
# Minimum 8 characters long, at least one uppercase and one lowercase letter, at least one digit

# Calls to validate password and then prompts user to see if they want to check their new password
# @var validatedPW saves return value of validatePW()
# @var checkPW checks for Y/y if user wants to print their set password
def main():
    validatedPW = validatePW()
    print("Password Successfully Set!")
    # *NOTE* may be required to check for inputs outside 'y'
    checkPW = input("Would you like to check your new password? (Y or N): ")
    if checkPW.lower() == "y":
        print("You current password is set to:", validatedPW)


# validates user entered password for the length, casing, whitespace and numbers.
# @var password prompts user to enter password which is then used to check for the required parameters
def validatePW():
    # loop runs until all parameters are met.
    print("When selecting your password, please keep the following requirements in mind:\n",
          "\033[1mLength: \033[0mMust use at least eight characters without spaces.\n",
          "\033[1mCharacters: \033[0mUse at least one uppercase letter, one lowercase letter and one number.")
    while True:
        password = input("Please enter a new password: ")
        if len(password) < 8:
            print("Password length needs to be 8 characters or longer.")
        # checks for spacing.
        elif password.count(' ') > 0:
            print("Password may not contain any spaces.")
        elif not any(char.isdigit() for char in password):
            print("Password needs to contain at least one number.")
        elif not any(char.isupper() for char in password):
            print("Password needs to contain at least one uppercase letter.")
        elif not any(char.islower() for char in password):
            print("Password needs to contain at least one lowercase letter.")
        # exits loops once all if statements return true
        else:
            break
    # loop runs until user re-enters the appropriate password.
    while True:
        reEnter = input("Please re-enter your password: ")
        if reEnter != password:
            print("Passwords do not match.")
        else:
            break
    # returns password to be used in main function to display it is the user wants.
    return password


main()
