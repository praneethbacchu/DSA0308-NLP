import re

text = """
Student Details:
Name: John Doe
Email: john.doe123@gmail.com
Mobile: +91-9876543210
Password: P@ssw0rd123
Date of Birth: 15/08/2004
Register Number: 23AIML1056
Department: Artificial Intelligence and Machine Learning
"""

# Regular Expression Patterns
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
mobile_pattern = r'\+91-\d{10}'
password_pattern = r'[A-Za-z0-9@#$%^&*!]+'
dob_pattern = r'\d{2}/\d{2}/\d{4}'
register_pattern = r'\d{2}[A-Z]{4}\d{4}'

print("Email ID:")
print(re.findall(email_pattern, text))

print("\nMobile Number:")
print(re.findall(mobile_pattern, text))

print("\nPassword:")
password = re.search(r'Password:\s*(\S+)', text)
print(password.group(1))

print("\nDate of Birth:")
print(re.findall(dob_pattern, text))

print("\nRegister Number:")
print(re.findall(register_pattern, text))
