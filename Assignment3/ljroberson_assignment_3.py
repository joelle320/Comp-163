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
emergency_contact = ("Mom", "Melissa Towns", "773-655-3749")
home_address = ("3146 223rd Street", "Sauk Village", "IL", "60411")
instagram_info = ("Instagram", "@laur.joelle", 873)
twitter_info = ("Twitter", "@laurjoelle", 7)
birthday = ("Birthday", 3, 20, 2007)

# Interest Tracking
current_skills_set = {"JavaScript", "HTML/CSS", "Git", "Time Management", "Problem Solving"}
skills_to_learn_set = {"React", "Data structures", "Web design", "Public speaking", "Python"}
career_interests_set = {"Software Development", "Web Development", "Data Science", "Game Development"}
hobbies_set = {"Gaming", "Crochet", "Reading", "Choir", "Music"}
entertainment_backlog_set = {"One Piece", "Naruto", "Fruits Basket", "IT", "ET"}

# Organizational Mapping
course_credits = {"COMP 163": 3, "MATH 110": 4, "ENGL 100": 3, "HIST 106": 3, "GEEN 111": 4, "FRST 101": 1}
course_professors = {"COMP 163": "Prof. Rhodes", "MATH 110": "Dr. Johnson", "ENGL 100": "Dr. Jefferson", "HIST 106": "Dr. Dovoe", "GEEN 111": "Dr. Parrish", "FRST 101": "Prof. Barrow"}
course_rooms = {"COMP 163": "M-Eric 300", "MATH 110": "Marteena 201", "ENGL 100": "Online", "HIST 106": "Online", "GEEN 111": "McNair 240", "FRST 101": "Online"}
monthly_budget = {"Food": 200, "Entertainment": 135, "Books": 0, "Transportation": 150}
study_hours = {"Programming": 4, "Math": 6, "English": 2, "History": 3}
contact_directory = {"Mother": "773-655-3749", "Roommate": "436-565-7043", "Academic Advisor": "336-334-5067"}

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