# Week 1.2, Session 2: Task 6

try:
    temperature = int(input("Enter the machine's temperature in degrees: "))
    pressure = int(input("Enter the machine's pressure in PSI: "))
    op_stat = int(input("Enter 1 if the machine is operating and 2 if it is not: "))
except:
    print("Invalid input")

if temperature > 80:
    temp="high"
    print("Temperature too high, it is a good idea to shut down the machine")
elif temperature > 50:
    print("Temperature within safe limits")
else:
    print("Machine temperature is low, no action needed")

if pressure > 100:
    press = "high"
    print("High pressure detected, maintainence recommended")
elif pressure > 70:
    print("Pressure is stable")
else:print("Pressure is low, system is operating normally")

if op_stat == 1 and (temp == "high" or press == "high"):
    print("Machine is running in unsafe conditions, it is recommended to shut it down")
elif op_stat ==1:
    print("Machine is running normally, no action needed")
else:
    print("Machine is stopped, no immediate action needed")