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
            if name == "":
                raise ValueError("Name cannot be an empty string")
            self.name = name
            self.birth = birth
        except:
            raise ValueError("Name cannot be an empty string")

    def initials(self):
        """
        Identifies the person's initials based on their given name
        """
        initial = ''.join([x[0].upper() for x in self.name.split(' ')])
        return initial

            
    def is_birthday(self):
        """
        Decides if the person's birthday is today or not, returns a
        boolean value
        """
        today = date.datetime.today()
        return today == self.birth