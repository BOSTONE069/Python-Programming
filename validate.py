import re

email = input("What is your email address? ").strip()

if re.search("^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")
