# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

import math

class Point:
    """
    A Point in 2D space.
    """
        def __init__(self, x, y)
            self.x = x
            self.y = y

        def distance(self):
            return math.hypot(self.x, self.y)
 
        def distance_to(self, point)):
            """
            Returns distance from this point to the specified point
            """
            return math.hypot(self.x - point.x, self.y - point.y

class Circle:
    """
    A circle
    """
    def __init__ (self, radius, centre=Point(0.0,0.0)):
    self.radius = radius
    self.cenre = centre

    def area (self):
        """
        Returns area of this circle
        """
        return math.pi*(self.radius)*(self.radius)

