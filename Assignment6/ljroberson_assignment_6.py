#OpenAI. (2025) ChatGPT (GPT-5-mini). Retrieved October 19, 2025, from chatgpt.com. I used ChatGPT to get help on project desccription in README and debugging Python logic errors related to the structure of my loops. Additionally, ChatGPT also helped by breaking down why certain string methods were necessary in different parts of the code.

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
contacts_list = []
for i, contact in enumerate(contacts, start=1):
    fields = contact.split('|') 
    if len(fields) == 4:
        name = fields[0].strip().title()
        phone = fields[1].strip()
        email = fields[2].strip().lower()
        address = fields[3].strip().title()

        # Step 3: Phone Number Standardization
        digits_only = ""
        for char in phone:
            if char.isdigit():
                digits_only += char
        if len(digits_only) == 10:
            phone = f"({digits_only[0:3]}) {digits_only[3:6]}-{digits_only[6:10]}"
        else:
            phone = "Invalid number"

        # Step 4: State Detection
        address_parts = fields[3].strip().split()
        for j in range(len(address_parts)):
            if len(address_parts[j]) == 2 and address_parts[j].isalpha():
                address_parts[j] = address_parts[j].upper()
            else:
                address_parts[j] = address_parts[j].title()
        address = " ".join(address_parts)
       
        print(f"\nCONTACT {i}:")
        print(f"Name: {name}")
        print(f"Phone: {phone}")
        print(f"Email: {email}")
        print(f"Address: {address}")

        contacts_list.append((name, phone, email))
    else:
        print(f"Invalid:", contact)
    
# Step 5: Professional Formatting/Alignment
print("\n=== DIRECTORY SUMMARY ===")
print(f"Total contacts processed: {len(contacts_list)}")

print("\n=== FORMATTED FOR PRINTING ===")
for name, phone, email in contacts_list:
    parts = name.split()
    if len(parts) == 2:
        last, first = parts[1], parts[0]
        formatted_name = f"{last}, {first}"
    else:
        formatted_name = name

    print(f"{formatted_name:<30}{phone:<20}{email}")