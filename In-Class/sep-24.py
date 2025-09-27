name = None
backup_name = "Guest"
list1 = [1,2,3]
list2 = list1

name_empty = name is None
backup_exists = backup_name is not None


sick_students = ["5123", "5124", "5345"]
assigned_bus = "BUS_A"

has_permission_slip = True
student_id = "5111"
student_bus = "BUS_A"

# can_ride_bus = has_permission_slip and not in sick_students

can_ride_bus = has_permission_slip and (student_bus == assigned_bus) and (student_id in sick_students)
print(can_ride_bus)