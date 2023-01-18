# Jacob L Stewart
# Chapter 3 Assignment 41
# Calculates are suggested tip based on order total and customer satisfaction:

def assignment03_41():
    # prompts user for order total and satisfaction rating 1-3
    orderTotal = float(input("How much was your dinner total: "))
    satisfaction = float(input("Please input your rating. 1 = Totally satisfied, 2 = Satisfied, 3 = Dissatisfied: "))

    # calculates tip based on satisfaction level provided
    SATLVL1 = ("${:.2f}".format(orderTotal * 0.20))
    SATLVL2 = ("${:.2f}".format(orderTotal * 0.15))
    SATLVL3 = ("${:.2f}".format(orderTotal * 0.10))

    # compares satisfaction level given and displays suggested tip accordingly
    if satisfaction == 1:
        # print("you answered 1.")
        print("Totally Satisfied, Suggested tip:", SATLVL1)
    elif satisfaction == 2:
        # print("you answered 2.")
        print("Satisfied, Suggested tip:", SATLVL2)
    else:
        # print("you answered 3.")
        print("Dissatisfied, Suggested tip:", SATLVL3)


assignment03_41()
