"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Caleb Cooke
"""
systime = 0
states = { "red":4, "red_amber":3, "green":5, "amber":3 }
time = 0

maxtime = int(input())  # read an integer number of steps (>0)
time = 1

while time <= maxtime:
    if systime <=15:
            if systime <= 3:
                print(f"Time {time:03} State red")
            elif systime <=6:
                print(f"Time {time:03} State red_amber")
            elif systime <= 11:
                print(f"Time {time:03} State green")
            elif systime <= 14:
                print(f"Time {time:03} State amber")
            time = time + 1
            systime = systime + 1
    else:
        time = systime
        systime = 0

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14