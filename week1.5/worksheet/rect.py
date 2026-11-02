# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """

        if not isinstance ((width, height), (int, float)):
            raise TypeError("Width and height must be a number")
        elif width <= 0 and height <= 0:
            raise ValueError("Width and height must be more than 0")
        else:
            self.width = width
            self.height = height

    def is_square(self):
       """
       Returns whether the rectangle is a square, as a boolean value
       given the values for height and width
       """
       return self.height == self.width

    def area(self):
        """
        Returns the area of the rectangle given the values for height
        and width
        """
        return (self.height)*(self.width)

    def perimeter(self):
        """
        Returns the perimeter of the rectangle, given the values for
        height and width
        """
        return 2*(self.height) + 2*(self.width)