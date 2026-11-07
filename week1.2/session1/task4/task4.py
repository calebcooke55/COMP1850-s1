# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetables)
print(both)
#Will print tomato

# Why does the following code diplay five items?

food = fruit.union(vegetables)
print(food)
#Because it is counting how many items are in fruit and vegetables, ignoring duplicates

# Add an item to fruit
fruit.add("strawberry")

# Remove an item from vegetables
vegetables.discard("tomato")

# Find and display symmetric difference of the two sets
print(vegetables.symmetric_difference(fruit))