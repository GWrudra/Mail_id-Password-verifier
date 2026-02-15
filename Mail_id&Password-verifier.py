import re

def email():
    while True:
        email_id = input("Enter your email ID: ")
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email_id) is not None:
            print("Email created")
            break
        else:
            print("Please enter a valid email.")


def check(key):
    if len(key) < 8:
        print("Password strength should be at least 8 characters.")
        return True
    elif not any(char.isdigit() for char in key):
        print("Password should contain at least one number.")
        return True
    elif not any(char.islower() for char in key):
        print("Password should contain at least one lowercase letter.")
        return True
    elif not any(char.isupper() for char in key):
        print("Password should contain at least one uppercase letter.")
        return True
    elif not any(char in '!@#$%^&*_:"?' for char in key):
        print("Password should contain at least one special character.")
        return True
    else:
        print("Password created successfully.")
        return False


def password():
    res = True
    while res:
        pasw = input("\nEnter your password: ")
        res = check(pasw)
    while True:
        confirm_pass = input("\nPlease confirm your password: ")
        if pasw == confirm_pass:
            print("Email and password generated successfully.")
            break
        else:
            print("Passwords do not match. Please try again.")


email()
password()