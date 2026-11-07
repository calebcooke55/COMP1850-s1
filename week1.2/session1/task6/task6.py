# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music = {"Racing Mount Pleasant":["Racing Mount Pleasant","Grip Your Fist, I'm Heaven Bound"], "Noah Kahan":["The Great Divide", "Stick Season", "I Was / I Am", "Busyhead"], "Tooth":["Restless in Bloom"]}

# Pretty-print the data structure
pprint(music)

# Display details of one album recorded by a specific artist
rmpalbums = music.get("Racing Mount Pleasant")
print(rmpalbums[1])