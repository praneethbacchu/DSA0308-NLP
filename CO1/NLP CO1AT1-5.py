import re

emails = [
    "john@gmail.com",
    "student123@yahoo.in",
    "invalidmail.com",
    "admin@college.edu",
    "abc@xyz",
    "nlp_user@gmail.com"
]

pattern = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|org|edu|in)$')

print("Email Validation Result\n")

for email in emails:
    if pattern.fullmatch(email):
        print(email, "-> Valid")
    else:
        print(email, "-> Invalid")


