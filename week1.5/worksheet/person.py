# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        Creates a profile for a person, storing their name and birth
        """
        try:
            if not isinstance (name, str):
                raise TypeError("Name must be a string")
            if not isinstance (birth, date):
                raise TypeError("Birthday must be a date")
            self.name = name
            self.birth = birth
        except:
            raise ValueError("Name cannot be an empty string")

    def initials(self):
        """
        Identifies the person's initials based on their given name
        """
        initial=[]
        for i in self.name:
            if self.name(i) - 1 == " ":
                initial.append(self.name(i))
            
    def is_birthday(self):
        """
        Decides if the person's birthday is today or not, returns a
        boolean value
        """
        today = date.today()
        return today == self.birth


    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
