Step 1
student_name = "Lauren Roberson" 
current_gpa = 3.0
study_hours = 20
social_points = 23
stress_level = 80

print(f"Welcome, {student_name}, to College Life Adventure!")
print("--- Current Stats ---")
print(f"Student: {student_name}")
print(f"GPA: {current_gpa}")
print(f"Study hours: {study_hours}")
print(f"Social points: {social_points}")
print(f"Stress level: {stress_level}")
print("---------------------")

#Step 2
print("Choose your course load:")
print("A) Easy (12 credits)")
print("B) Medium (15 credits)")
print("C) Hard (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    if current_gpa <= 2.5:
        print(f"Chosen Course Load: {choice} This should be a safe option with your GPA.")
    else:
        print(f"Chosen Course Load: {choice} You could probably handle a harder difficulty, but it's your choice!")
elif choice == "B":
    if current_gpa >= 2.0:
        print(f"Chosen Course Load: {choice} A medium level difficulty course load should work fine.")
    else:
        print(f"Chosen Course Load: {choice} This may be a challenge with your GPA.")
elif choice == "C":
    if current_gpa >= 3.5:
        print(f"Chosen Course Load: {choice} You have a great GPA! You can handle a high level difficulty course load.")
    else:
        print(f"Chosen Course Load: {choice} This level difficulty course load might be too stressful with your GPA.")
else:
    print("Invalid input. Please choose A, B, or C.")

