def calculate_tip(bill_amount, tip_percentage):
    # Example Docstring
    """
    Calculate the tip amount based on the bill amount and tip percentage.

    Parameters:
    bill_amount (float): The total bill amount.
    tip_percentage (float): The tip percentage to be applied.

    Returns:
    float: The calculated tip amount.
    """
    tip_amount = bill_amount * (tip_percentage / 100)
    return tip_amount

def check_grade(score):
    # Example Docstring
    """
    Determine if student passes or fails based on the numeric score.

    Parameters:
    score (float): The numeric score (0-100).

    Returns:
   Pass or Fail
    """

    if score >= 70:
        return "Pass"
    else:
        return "Fail"
    
def add_three_numbers(a, b, c):
        # Example Docstring
        """
        Add three numbers together.

        Parameters:
        a (float): The first number.
        b (float): The second number.
        c (float): The third number.

        Returns:
        float: The sum of the three numbers.
        """
        return a + b + c
result = add_three_numbers(10, 20, 30)
print("The sum of the three numbers is:", result)

def create_email(first_name, last_name):
    # Example Docstring
    """
    Create an email address based on the first name, last name, and domain.

    Parameters:
    first_name (str): The first name of the user.
    last_name (str): The last name of the user.

    Returns:
    str: The constructed email address.
    """
    email = f"{first_name.lower()}{last_name.lower()}@ncat.edu"
    return email
result = create_email("Lauren", "Roberson")
print("The generated email address is:", result)

def check_voting_age(age):
    # Example Docstring
    """
    Check if a person is eligible to vote based on their age.

    Parameters:
    age (int): The age of the person.

    Returns:
    str: A message indicating voting eligibility.
    """
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."
result = check_voting_age(20)
print(result)
result = check_voting_age(16)
print(result)

def add_course(course_list,new_course):
    # Example Docstring
    """
    Add a new course to the list of courses.

    Parameters:
    course_list (list): The list of current courses.
    new_course (str): The new course to be added.

    Returns:
    list: The updated list of courses.
    """
    course_list.append(new_course)
    return course_list
result = add_course(["MATH 150", "ENGL 101"], "COMP 163")
print("Updated course list:", result)

def is_valid_password(password):
    # Example Docstring
    """
    Check if the password meets the minimum length requirement.

    Parameters:
    password (str): The password to be checked.

    Returns:
    bool: True if the password is valid, False otherwise.
    """
    if len(password) >= 8:
        return True
    else:
        return False
print("Is the password valid?", ("hello123"))
print("Is the password valid?", ("hi"))

# Calculator
def add(a, b):
    """Addition with two numbers."""
    return a + b
def subtract(a, b):
    """Subtraction with two numbers."""
    return a - b
def multiply(a, b):
    """Multiplication with two numbers."""
    return a * b
def divide(a, b):
    """Division with two numbers."""
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."
def calculator(num1, num2, operation):
    """ 
        Simplistic Calculator

        Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").

        Returns:
        float: The result of the operation. If division by zero, returns an error message.
    """
    if operation == "add":
        return add(num1, num2)
    elif operation == "subtract":
        return subtract(num1, num2)
    elif operation == "multiply":
        return multiply(num1, num2)
    elif operation == "divide":
        return divide(num1, num2)
    else:
        return "Invalid operation."
result = calculator(10, 5, "add")
print("Addition Result:", result)
result = calculator(10, 5, "subtract")
print("Subtraction Result:", result)
result = calculator(10, 5, "multiply")
print("Multiplication Result:", result)
result = calculator(10, 5, "divide")
print("Division Result:", result)
result = calculator(10, 0, "divide")
print("Division Result:", result)







