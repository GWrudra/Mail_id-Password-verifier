import re

def get_email():
    while True:
        email = input("Enter your email ID: ")
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            print("Email accepted!")
            return email
        print("Invalid email format — try again.")

def valid_password(pw):
    if len(pw) < 8:
        print("Must be at least 8 characters.")
        return False
    if not any(c.isdigit() for c in pw):
        print("Must contain a digit.")
        return False
    if not any(c.islower() for c in pw):
        print("Must contain a lowercase letter.")
        return False
    if not any(c.isupper() for c in pw):
        print("Must contain an uppercase letter.")
        return False
    if not any(c in "!@#$%^&*_-+?." for c in pw):
        print("Must contain a special character.")
        return False
    return True

def get_password():
    while True:
        pw = input("Enter a strong password: ")
        if valid_password(pw):
            confirm = input("Confirm password: ")
            if pw == confirm:
                print("Password confirmed!")
                return pw
            print("Passwords don’t match. Try again.")

if __name__ == "__main__":
    get_email()
    get_password()
    print("\nDone ✅")