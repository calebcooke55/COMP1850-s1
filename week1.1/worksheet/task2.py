"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Caleb Cooke
"""

import sys

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")
try:
    amount = int(input("How much do you want to save every month? :"))
except TypeError:
    sys.exit("Invalid amount")
except ValueError:
    sys.exit("Invalid amount")
end_year = amount * 12
print(f"The amount you will have saved by the end of the year is £{end_year:.2f}")
with_interest = end_year*1.008
print(f"The total amount of money including interest will be £{with_interest:.2f}")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

