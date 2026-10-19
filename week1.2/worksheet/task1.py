# Worksheet 1.2: Task 1 Solution

import sys

try:
    integer = int(input("Please enter an integer between 0 and 100"))
    if integer >=0 and integer <=100:
        if integer >=70:
            print(integer, "is a Distinction")
        elif integer >= 40:
            print(integer, "is a Pass")
        else:
            print(integer, "is a Fail")
    else:
        sys.exit("Error: Grade must be an integer between 0 and 100")
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")