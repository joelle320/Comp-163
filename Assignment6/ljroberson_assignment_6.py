# ljroberson_assignment_6.py
# Student: Lauren Roberson
# Assignment 6: Contact Information Formatter

# Step 1: Initial Setup
print("Enter contact information (format: name|phone|email|address):")
print(f"\n=== CONTACT DIRECTORY ===")
contacts = []
while True:
    contact = input().strip()
    contacts.append(contact)
    if contact == "DONE":
        break
contacts = contacts[:-1]
# Step 2: Name/Address Cleaning
for i, contact in enumerate(contacts, start=1):
    fields = contact.split('|') 
    if len(fields) == 4:
        name = fields[0].strip().title()
        phone = fields[1].strip()
        email = fields[2].strip().lower()
        address = fields[3].strip().title()

        # Step 3: Implement phone number standardization
        digits_only = ""
        for char in phone:
            if char.isdigit():
                digits_only += char
        if len(digits_only) == 10:
            phone = f"({digits_only[0:3]}) {digits_only[3:6]}-{digits_only[6:10]}"
        else:
            phone = "Invalid number"
            
        print(f"\nCONTACT {i}:")
        print(f"Name: {name}")
        print(f"Phone: {phone}")
        print(f"Email: {email}")
        print(f"Address: {address}")
    else:
        print(f"Invalid:", contact)