# Week 4, Session 1: 

# There are 5 functions defined below, one for each arithmetic operation
# and one for getting user inputs. Please inspect the code and then
# complete the code for case 1 to case 4.

#------------------------------------------------------------------
#FUNCTION DIRECTORY:
def addition(num1, num2):
    """ adds together 2 given numbers"""
    return num1 + num2

def subtraction(num1, num2):
    """subtracts one given number from another"""
    return num1 - num2

def multiplication(num1, num2):
    """Multiplies 2 givem numbers together"""
    return num1 * num2

def division(num1, num2):
    """
    Divides one given number by another
    Returns an error if this is not possible
    """
    if num2 == 0:
        return "Error: cannot divide by zero"
    else:
        return num1 / num2

def run_program():
    # Ask user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask user for the desired operation
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = int(input("Enter your choice (1-4): "))

    match operation:
    """
    Asks user to enter their choice of which operation to perform
    Performs this operation with the given numbers
    Returns the output of this operation
    """
        case 1:
            result = None 
            numbers = int(input("Please enter the numbers you would like to perform this operation with: "))
            result = addition(numbers)   # complete this line of code
            print(f"The result of addition is: {result}")
        case 2:
            result = None    # complete this line of code
            print(f"The result of subtraction is: {result}")
        case 3:
            result = None   # complete this line of code
            print(f"The result of multiplication is: {result}")
        case 4:
            result = None    # complete this line of code
            print(f"The result of division is: {result}")
        case _:
            print("Undefined operation")

#------------------------------------------------------------------
#IMPLEMENTATION:
run_program()


# In the function run_program, they are more than one tasks involved:
#   (1) getting user input for numbers
#   (2) ask user for desired operation
#   (3) match operation.

#    If you are to split each task into a separate function, how would you
#   name the function for each of these tasks?
