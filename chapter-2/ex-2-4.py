# Programming Exercise 2-4
#
# Program to compute a final price for five items with tax.
# This program will prompt a user for a set of five prices,
# sum them to a subtotal and calculate sales tax with tax rate stored in a constant,
# then display the results on the screen.

# Variables to hold the prices of five items, the subtotal, and the total.
# All should be initialized as floats.

# Constant for the sales tax rate.
tax_rate = .06

# Get the price of each item by prompting the user.
# You will need to convert each input to a float
item1 = float(input("What is the first price?: "))
item2 = float(input("what is the second price?: "))
item3 = float(input("What is the third price?: "))
item4 = float(input("What is the fourth price?: "))
item5 = float(input("What is the fifth price?: "))

# Calculate the subtotal by adding up the item prices.
subtotal = item1 + item2 + item3 + item4 + item5

# Calculate the sales tax by multiplying the subtotal by the tax rate.
tax = subtotal * tax_rate

# Calculate the total by adding the subtotal and tax.
total = subtotal + tax

# Print the values for the subtotal, tax and total.
# Label each value, and format them to display with two decimal places. 
print(subtotal), {.2}
print(tax), {.2}
print(total), {.2}


