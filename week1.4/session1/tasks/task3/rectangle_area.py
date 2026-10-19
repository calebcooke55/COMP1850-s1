
# function implementation:

x = int(input("Enter width of rectangle:"))
y = int(input("Enter length of rectangle:"))
area = rectangle_area(x,y) #calls function rectangle_area with the parameters x and y
print("The area of the rectangle is", area)


def rectangle_area(a,b):
    """
    Takes in width and height of a rectangle and returns the area of the rectangle
    """
    c = a*b
    return c

#accept an integer value and returns a list of even integers between 0 and that value.​

def listing(x):
    """
    Returns a list of even numbers from 0 up to the given limit
    """
    return[n for n in range(x+1) if n % 2 ==0]


user_int = int(input("Enter an integer value"))
list_int = listing(user_int)
print(list_int)

#Accepts a list of integers and returns the mean average of the list
#list_int = input("Enter some numbers, separated by spaces: ")
#numbers = [float(item) for item in list_int.split()]

    