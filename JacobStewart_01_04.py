# Jacob L Stewart
# Chapter 1 Assignment 04
# Printing balance of an account with 5% interest over 3 years.

# variables for calculating
curBal = 1000
RATE = 0.05

# Prints initial balance with line break
print("Current Balance:", curBal, "\n", "--------------")

# Formula for compound interest rounded for easier reading
print("Year 1:", round(curBal*pow((1+RATE/1), 1*1), 2))
print("Year 2:", round(curBal*pow((1+RATE/1), 1*2), 2))
print("Year 3:", round(curBal*pow((1+RATE/1), 1*3), 2))
