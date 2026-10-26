# Student Class

# Attributes
# - Name
# - Course (degree programme)
# - Student ID number
# - Email

# Behaviour
# - Goes to lectures
# - Submits a portfolio task
# - Enrol on a module


#-- DEFINING A PYTHON CLASS --
#1. Start with the class keyword
#|   Names should be in upper camel case (sentence case w/o spaces)
#2. Beneath that, we write the methods
#|   Use snake case for methods

class Point:
    """
    A point in 2D space
    """
    def __init__(self, x, y):
        """
        Creates a point, given x & y coordinates
        """
        self.x = x
        self.y = y
    def distance(self):
        """
        Returns distance from this point to the origin
        return math.hypot(self.x, self.y)
        """