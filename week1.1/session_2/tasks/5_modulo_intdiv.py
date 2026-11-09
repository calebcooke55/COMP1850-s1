
# This program takes a file which contains students IDs and the hours late that work was submitted
#It returns the amount of time late the assignment was in days, hours and minutes

with open("_data/lateness_data.csv") as f:
    data = f.readlines()

data = [line.strip().split(",") for line in data]

for row in data:
    minutes_late = int(row[1])

    hours = (minutes_late//60)%24
    days = (minutes_late//60)//24
    minutes = minutes_late%60
    
    print(f"Student {row[0]}: {days}D {hours}H {minutes}M")

