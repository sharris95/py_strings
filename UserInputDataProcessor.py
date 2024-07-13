#User Input Dataa Processor

def validate_name(name, name_type):
    if len(name) < 2:
        print(f"Error: {name_type} must be at least 2 characters long.")
        return False
    return True

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

if validate_name(first_name, "First name") and validate_name(last_name, "Last name"):
    print("Both names are valid.")
else:
    print("Please enter valid names.")