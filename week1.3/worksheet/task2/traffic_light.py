"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided time code, was written and developed by you independently.
Name: Caleb Cooke
"""
time = 0
systime = 0
states = { "red":4, "red_amber":3, "green":5, "amber":3 }

maxtime = int(input())  # read an integer number of steps (>0)
systime = 1

while systime <= maxtime:
    if time <=15:
            if time <= 3:
                state = "red"
                print(f"Time {systime:03} State {state}")
            elif time <=6:
                state = "red_amber"
                print(f"Time {systime:03} State {state}")
            elif time <= 11:
                state = "green"
                print(f"Time {systime:03} State {state}")
            elif time <= 14:
                state = "amber"
                print(f"Time {systime:03} State {state}")
            systime = systime + 1
            time = time + 1
    else:
        systime = time
        time = 0

# Simulate the traffic light system up to systime=maxtime in 1-second steps

# At the end of each step you should output the systime and state using the statement on line 14