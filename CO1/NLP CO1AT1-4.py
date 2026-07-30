import re

email = input("Enter Email ID: ")
password = input("Enter Password: ")

email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|org|edu|in)$'

password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*!]).{8,}$'

# Email Validation
if re.fullmatch(email_pattern, email):
    print("\nEmail ID is Valid")
else:
    print("\nEmail ID is Invalid")

# Password Validation
if re.fullmatch(password_pattern, password):
    print("Strong Password")
else:
    print("Weak Password")
