#Step 1
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

#Step 4
print("--- Final Semester Assessment ---")
print("Make your final choice to determine the outcome of the semester!")
print("A) Focus on grades")
print("B) Focus on social life")
print("C) Balance both")

final_choice = input("Your choice: ")

research_opportunity = "A"
social_opportunity = "B"
balance_opportunity = "C"
opportunity_type = final_choice

if type(current_gpa) == float:
    if opportunity_type == research_opportunity:
        if current_gpa >= 3.5 and stress_level < 50:
            print("Ending 1: You aced this semester! Your GPA and stress are manageable.")
        else:
            print("Ending 2: You focused on grades but stress took a toll. Remember to balance next time.")
    elif opportunity_type == social_opportunity:
        if social_points >= 30:
            print("Ending 3: Your social life is amazing but your GPA suffered.")
        else:
            print("Ending 4: You tried to socialize but didn’t do the best.")
    elif opportunity_type == balance_opportunity:
        if study_hours >= 20 and social_points >= 30:
            print("Ending 5: You pretty much balanced academics and your social life.")
        else:
            print("Ending 6: You aimed for balance but could work on time management.")
    elif opportunity_type != research_opportunity and opportunity_type != social_opportunity and opportunity_type != balance_opportunity:
        print("Invalid choice. No final outcome determined.")
else:
    print("Error: GPA type invalid, cannot determine final outcome.")

print("--- Final Status ---")
print(f"Student: {student_name}")
print(f"GPA: {round(current_gpa,2)}")
print(f"Study hours: {study_hours}")
print(f"Social points: {social_points}")
print(f"Stress level: {stress_level}")
print("-------------------")