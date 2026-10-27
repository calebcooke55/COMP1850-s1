"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided time code, was written and developed by you independently.
Name: Caleb Cooke
"""

import sys
time = 0
systime = 0
states = { "red":4, "red_amber":3, "green":5, "amber":3 }

try:
    maxtime = int(input("Please enter an integer number of steps:"))  # read an integer number of steps (>0)
except TypeError:
    print("Invalid input")

while systime <= maxtime:
    if time <15:
            if time < 4:
                state = "red"
                print(f"Time {systime:03} State {state}")
            elif time < 7:
                state = "red_amber"
                print(f"Time {systime:03} State {state}")
            elif time < 12:
                state = "green"
                print(f"Time {systime:03} State {state}")
            elif time <= 15:
                state = "amber"
                print(f"Time {systime:03} State {state}")
            systime = systime+1
            time = time + 1
    else:
        time = 0
sys.exit()

# Simulate the traffic light system up to systime=maxtime in 1-second steps

# At the end of each step you should output the systime and state using the statement on line 14