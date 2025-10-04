item = 0
# userInput = bool(input())
# command = userInput
# if command == true:
# while command == false:
#     if item % 2 == 0:
#         item += 2
#         print(item)
#         if  command == "quit":
#             break

for item in range(1,11):
    if item % 3 == 0:
        continue
    print(item)

print("-------------------------------")

class_list = ["Shon", "Josh", "Sage", "Tati", "Elias"]
student = "Josh"
for student in class_list:
    if student != "Josh":
        continue
    print(f"Found {student}!")
else:
    print("{student} is not in the class.")