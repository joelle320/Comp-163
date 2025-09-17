# Tuples
fruits = ("pear", "blackberry", "cherry")
print(fruits[0])
print(len(fruits))

fruits2 = "pear", "blackberry", "cherry"
print(fruits2[0])
print(len(fruits2))

# Sets
colors = {"red", "blue", "gold", "silver"}
colors.add("yellow")
print(colors)

# Dictionaries
student = {
    "Name": "Ben",
    "Age": 20,
    "Major": "Computer Science"
}
print(student["Name"])

# Challenge 
zoo_animals = ["lion", "elephant", "penguin", "giraffe"]
arctic_animals = {"penguin", "seal", "polar bear"}
bird_info = ("eagle", 3.2, "golden")
animal_counts = {
    "lions": 2,
    "elephants": 4,
    "penguins": 6,
    "giraffes": 3
}

print(f"Zoo Animals: {zoo_animals}")
print(f"Arctic Animals: {arctic_animals}")
print(f"Bird Info: {bird_info}")
print(f"Animal Counts: {animal_counts}")
