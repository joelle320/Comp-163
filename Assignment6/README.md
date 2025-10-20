# Assignment 6

# Author
Lauren Roberson – COMP 163, Fall 2025

# Description
This project includes one Python program that processes and formats contact information entered by the user by using string manipulation, loops, conditionals, etc.

Contact Information Formatter

- Accepts multiple contact entries in the format name|phone|email|address until the user types DONE.

- Cleans and formats each contact’s name, phone number, email, and address.

- Displays all contact details in a neatly organized output and provides a summary showing the total number of contacts processed.

# How It Works

- Input: The program collects contact information until the user types DONE.

- Data Cleaning: It trims extra spaces, capitalizes names and addresses, and converts emails to lowercase.

- Phone Formatting: Removes all non-digit characters and reformats valid 10-digit numbers into (XXX) XXX-XXXX.

- Address Formatting: Detects two-letter state abbreviations and converts them to uppercase while capitalizing other words.

- Output: Prints each formatted contact, followed by a directory summary and a printable list.

# AI Help

I used ChatGPT (OpenAI, 2025) to improve the logic behind the structure of my loops, simplify variable names, and ensure the output formatting matched the expected output for the test cases. I also asked AI to polish my README by providing suggestions for the projects description. 

## How to Run

Open the Assignment6 folder to access the Python file.
python ljroberson_assignment_6.py
To View Commits: https://github.com/joelle320/Comp-163/tree/main/Assignment6