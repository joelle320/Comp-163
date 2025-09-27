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

#Step 3
study_options = ["Programming", "Math", "English", "History"]

print("Choose a study focus from the list below:")
print(study_options)
user_study = input("Your choice: ")

if user_study in study_options:
    if (user_study is "Programming" or user_study is "Math") and current_gpa < 2.5:
        print(f"Your Choice: {user_study} You may struggle with technical/mathematical courses, so your GPA might drop a little.")
        current_gpa -= 0.2
        stress_level += 15
    elif user_study is not "Programming" and user_study is not "Math":
        print(f"Your Choice: {user_study} You chose a writing-heavy subject. Expect long nights of writing.")
        social_points += 5
        stress_level += 5
    else:
        print(f"Your Choice: {user_study} Good choice!")
        study_hours += 5
elif user_study not in study_options:
    print("Invalid choice. Please choose from the list.")
print(f"GPA:{round(current_gpa,2)}")
print(f"Study Hours: {study_hours}")
print(f"Stress Level: {stress_level}")
print(f"Social Points: {social_points}")