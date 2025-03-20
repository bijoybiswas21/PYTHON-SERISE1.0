# 1. Basic input with type validation
def get_user_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if 0 <= age <= 120:
                return age
            print("Please enter a valid age between 0 and 120")
        except ValueError:
            print("Please enter a number")

# 2. Multiple data input with validation
def get_student_info():
    name = input("Enter student name: ").strip()
    while not name:
        name = input("Name cannot be empty. Please enter name: ").strip()
    
    try:
        marks = float(input("Enter marks (0-100): "))
        if not 0 <= marks <= 100:
            marks = 0
    except ValueError:
        marks = 0
    
    return name, marks

# 3. Password input with confirmation
def get_password():
    while True:
        password = input("Enter password: ")
        confirm = input("Confirm password: ")
        if password == confirm and len(password) >= 6:
            return password
        print("Passwords don't match or too short (min 6 characters)")

# 4. Input with default values
def get_preferences():
    theme = input("Enter theme [dark/light] (default: dark): ").lower() or "dark"
    size = input("Enter size [small/medium/large] (default: medium): ").lower() or "medium"
    return theme, size

# 5. Data validation with custom rules
def get_email():
    while True:
        email = input("Enter email address: ").strip()
        if "@" in email and "." in email:
            return email
        print("Please enter a valid email address")

# Example usage
if __name__ == "__main__":
    age = get_user_age()
    name, marks = get_student_info()
    password = get_password()
    theme, size = get_preferences()
    email = get_email()
    
    print("\nCollected Data:")
    print(f"Age: {age}")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Theme: {theme}")
    print(f"Size: {size}")
    print(f"Email: {email}")