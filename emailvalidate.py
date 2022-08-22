import re

email = input("What is your email address? ").strip()

if re.search(r"^.+@.+\.com$", email):
    print("Valid")
else:
    print("Invalid")
