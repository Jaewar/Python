# Read the total book price and the number of books.
# Compute the tax (7.5 percent of the total book price).
# compute the shipping charge ($2 per book).
# The price of the order is the sum of the total book price, the tax, and the shipping charge.
# Print the price of the order


def assignment2_32():
    TAXRATE: float = 0.075
    # continuous loop that verifies that the input is an integer.
    while True:
        try:
            bookPrice = int(input("Input total price of order: "))
            # catches error and prompts user to reenter
        except ValueError:
            print("Error! Please enter a number. Try again.")
            # breaks out of current loop to retrieve second number
        else:
            try:
                totalBooks: int = int(input("Input number of books: "))
                # catches error and prompts user to reenter
            except ValueError:
                print("Error! Please enter a number. Try again.")
                # displays required equations after 2 integers are input.
            else:
                shippingCost = totalBooks * 2
                totalBookPrice = bookPrice + (bookPrice * TAXRATE)
                orderTotal = (totalBookPrice + shippingCost)
                print("Total price of order: $", round(orderTotal, 2))
            break
    # loop that verifies the input is an integer then displays required results


assignment2_32()
