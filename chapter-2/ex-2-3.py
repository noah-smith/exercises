# Programming Exercise 2-3
#
# Program to convert area in square feet to acres.
# This program will prompt a user for the size of a tract in square feet,
# then use a constant ratio value to calculate it value in acres
# and display the result to the user.

# Variables to hold the size of the tract and number of acres.
# be sure to initialize these as float
sq_ft = float(input("What is the size in square feet?: "))

# Constant for the number of square feet in an acre.
SQUARE_FEET_IN_ACRE = 46777

# Get the square feet in the tract from the user.
# you will need to convert this input to a float


# Calculate the number of acres
acres = sq_ft/SQUARE_FEET_IN_ACRE

# Print the number of acres.
# remember to format the acres to two decimal places
output = "Size in acres is: ", acres
print(output)





