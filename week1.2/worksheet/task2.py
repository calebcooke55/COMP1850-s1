# Worksheet 1.2: Task 2 Solution
import sys
import util

def median(numbers):
    length = len(numbers)
    if length%2 == 0:
        final1 = numbers[length//2]
        final2 = numbers[(length//2)-1]
        final =  (final1+final2)/2
    else:
        final = numbers(length//2)
    return(final)

from util import read_numbers
numbers = read_numbers()
numbers.sort()

minimum = min(numbers)
maximum = max(numbers)
mean = (sum(numbers))/(len(numbers))
median_r = median(numbers)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Mean =", mean)
print("Median =", median_r)


def med():
    length = len(numbers)
    if length%2 == 0:
        final = ((numbers(length//2-1) + numbers(length//2))/2)
    else:
        final = numbers(length//2)
    return(final)
