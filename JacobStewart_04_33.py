# Jacob L Stewart
# Chapter 4 Assignment 33
# Write an application to pre-sell a limited number of cinema tickets. Each buyer can buy as many as 4 tickets. No
# more than 100 tickets can be sold. Implement a program that prompts the user for the desired number of tickets and
# then displays the number of remaining tickets. Repeat until all tickets have been sold, and then display the total
# number of buyers.

def assignment04_33():

    # declares variable and prints to user total tickets available initially.
    totalTickets = 100
    print("There are currently", totalTickets, "ticket(s) available.")

    # Loop that runs until totalTickets reaches 0.
    while totalTickets > 0:
        try:
            ticketOrder = int(input("How many tickets would you like to purchase? (Maximum of 4 per customer) "))
            # checks that tickets ordered are not larger than 4
            if ticketOrder > 4:
                print("Only 4 tickets per customer may be purchased.")
            # if order is 4 or less, this checks that enough tickets are available for purchase
            elif ticketOrder > totalTickets:
                print("Apologies, the remaining amount of tickets available are:", totalTickets)
            # when previous conditions are met, removes tickets from overall amount and displays the remaining tickets
            else:
                totalTickets -= ticketOrder
                print("There are currently", totalTickets, "ticket(s) available.")
        # catches any input that isn't a whole number i.e. letters / decimals
        except ValueError:
            print("Please only enter the number of tickets requested. (Whole Number)")
    # when all tickets are purchased loop closes and closing message is displayed.
    print("All tickets have been purchased.")


assignment04_33()
