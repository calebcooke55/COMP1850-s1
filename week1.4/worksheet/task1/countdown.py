
import sys

def countdown(number): 
    '''  
    This recursive function takes a positive integer number  
    and counts the number down to zero printing each value. 
    ''' 
    if number == 0:
        return 0
    print(number) 
    return countdown(number-1)

try:
    x = int(input("Enter a positive integer number:"))
except:
    sys.exit("The number was not a positive integer")
    
if x <0:
    sys.exit("The number was not a positive integer")
else:
    print(countdown(x))