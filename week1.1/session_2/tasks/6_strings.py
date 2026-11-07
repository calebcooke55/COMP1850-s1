# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") #Prints the original string
print(f"Modified String 1: {user_string.lower()}") #Prints the string in lowercase
print(f"Modified String 2: {user_string.upper()}") #Prints the string in uppercase
print(f"Modified String 3: {user_string.strip()}") #Removes any spaces at the start or end of the string
print(f"Modified String 4: {user_string.replace('a', '@')}") #Prints the string, replacing any occurences of the "a" character with the "@ character"
print(f"Modified String 5: {user_string.capitalize()}") #Prints the string with sentence case
print(f"Modified String 6: {user_string[::-1]}") #Prints the string backwards
print(f"Modified String 7: {user_string.title()}") #Prints the string with the first letter of each word capitalised
print(f"Modified String 8: {len(user_string)}") #Prints the length of the string (number of characters including " ")
print(f"Modified String 9: {user_string.find('a')}") #Prints the index of the chosen character within the string
print(f"Modified String 10: {user_string.count('a')}") #Counts the number of occurences of the chosen character within the string
print(f"Modified String 11: {user_string.startswith('Hello')}") #Returns a boolean as to if the string begins with the provided word etc.
print(f"Modified String 12: {user_string.endswith('!')}") #Returns a boolean as to if the string ends with the provided word etc.
print(f"Modified String 13: {user_string.isalnum()}") #Returns a boolean as to if the string is alphanumberic (a-z or 1-9)
print(f"Modified String 14: {user_string.isalpha()}") #Returns a boolean as to if the string contains only letters a-z
print(f"Modified String 15: {user_string.isdigit()}") #Returns a boolean as to if the string contains only digits 1-9
