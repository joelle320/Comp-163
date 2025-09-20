# Personal Data Portfolio

# Personal Information Storage
full_name = "Lauren Roberson"
student_email = "ljroberson@aggies.ncat.edu"
hometown = "Chicago, IL"
graduation_semester = "Spring 2029"
major = "Computer Science"

# Academic Data Organization
current_courses = ["COMP 163", "MATH 110", "ENGL 100", "HIST 106", "GEEN 111", "FRST 101"]
completed_courses = ["AP Lang", "AP Pysch", "Pre-Calc", "Game Programming", "Web Design"]
credit_hours_list = [3, 1, 1, 3, 4, 4]
gpa_history = [3.2, 3.3, 4.0, 4.0]

# Contact Information Storage
emergency_contact = ("Mom", "Hannah Smith", "704-555-0199")
home_address = ("456 Oak Street", "Charlotte", "NC", "28202")
instagram_info = ("Instagram", "@jordan_codes", 312)
twitter_info = ("Twitter", "@jordandev", 127)
birthday = ("Birthday", 5, 22, 2006)

# Interest Tracking
current_skills_set = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn_set = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interests_set = {"Software development", "Web development", "Data science", "Game development"}
hobbies_set = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog_set = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

# Organizational Mapping
course_credits = {"COMP 163": 3, "MATH 150": 3, "ENG 101": 3, "HIS 105": 3}
course_professors = {"COMP 163": "Prof. Rhodes", "MATH 150": "Dr. Lee", "ENG 101": "Dr. Martinez", "HIS 105": "Dr. Brown"}
course_rooms = {"COMP 163": "M-Eric 300", "MATH 150": "Marteena 201", "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"}
monthly_budget = {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}
study_hours = {"Programming": 10, "Math": 8, "English": 4, "History": 3}
contact_directory = {"Mom": "704-555-0199", "Roommate": "336-555-7821", "Academic Advisor": "336-334-5000"}

# Required Calculations
total_credits = sum(credit_hours_list)
cumulative_gpa = sum(gpa_history) / len(gpa_history)
completed_courses_count = len(completed_courses)
total_weekly_study_hours = sum(study_hours.values())
academic_load = total_credits + total_weekly_study_hours
monthly_budget_total = sum(monthly_budget.values())
daily_food_budget = round(monthly_budget["Food"] / 30, 2)
annual_budget_projection = monthly_budget_total * 12
study_cost_per_hour = round(monthly_budget["Books"] / total_weekly_study_hours, 2)

# Analytics Calculations
total_social_media_followers = instagram_info[2] + twitter_info[2]
skills_comparison = (len(current_skills_set), len(skills_to_learn_set))
contact_directory_size = len(contact_directory)
entertainment_backlog_count = len(entertainment_backlog_set)
academic_workload_assessment = (total_credits, total_weekly_study_hours)

# Outputs 
print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")

print(f"Student: {full_name} | Email: {student_email}")
print(f"From: {hometown} | Graduating: {graduation_semester}")
print(f"Major: {major}")

print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {total_credits} credits across {len(current_courses)} courses")
print(f"Cumulative GPA: {cumulative_gpa:.2f}")
print(f"Weekly Study Time: {total_weekly_study_hours} hours")
print(f"Academic Investment: ${study_cost_per_hour} per study hour")

print("Current Courses:")
for course, credits in zip(current_courses, credit_hours_list):
    print(f"{course} - {credits} credits - {course_professors[course]} - {course_rooms[course]}")
print()

print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills_set}")
print(f"Learning Goals: {skills_to_learn_set}")
print(f"Career Interests: {career_interests_set}")
print(f"Skills Currently Have: {len(current_skills_set)}")
print(f"Skills Want to Learn: {len(skills_to_learn_set)}")

print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget_total}")
print(f"Food: ${monthly_budget['Food']} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthly_budget['Entertainment']}")
print(f"Books: ${monthly_budget['Books']}")
print(f"Transportation: ${monthly_budget['Transportation']}")
print(f"Annual Projection: ${annual_budget_projection}")

print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]}, {home_address[2]} {home_address[3]}")
print(f"Social Media Presence: {total_social_media_followers} followers across 2 platforms")
print(f"Key Contacts: {len(contact_directory)} people in directory")

print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {completed_courses_count}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {len(entertainment_backlog_set)} items")
print(f"Current Hobbies: {len(hobbies_set)} activities")
print("================================================================")