# Open a file called names.txt and print its contents

with open('names.txt', 'r') as file:
    contents = file.read()
    print(contents)

# Open a file called names.txt and print the third line

with open('names.txt', 'r') as file:
    lines = file.readlines()
    if lines:
        print(lines[2])  # Print the third line (index 2)