# ljroberson_assignment_6.py
# Student: Lauren Roberson
# Assignment 6: Contact Information Formatter

# Step 1: Initial setup
print("Enter contact information (format: name|phone|email|address):")

contacts = []
while True:
    contact = input().strip()
    contacts.append(contact)
    if contact == "DONE":
        break
contacts = contacts[:-1]

for contact in contacts:
    fields = contact.split('|') 
    if len(fields) == 4:
        name = fields[0]
        phone = fields[1]
        email = fields[2]
        address = fields[3]

        print(f"\n=== CONTACT DIRECTORY ===\n")
        print(f"Name: {name}")
        print(f"Phone: {phone}")
        print(f"Email: {email}")
        print(f"Address: {address}")
    else:
        print(f"Invalid:", contact)