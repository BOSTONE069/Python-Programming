import re

email = input("What is your email address? ").strip()

if re.search("^\w+@\w+\.com$", email):
    print("valid")
else:
    print("invalid")
