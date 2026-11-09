
# This programme asks a user to enter two numbers (one per input)
# multiplies those numbers together
# prints out the result

import sys

try:
    number1 = int(input("Please enter number 1"))
    number2 = int(input("Please enter number 2"))
except:
    sys.exit("That is not a number")

print(number1 * number2)
