import re

email = input("What is your email address? ").strip()

# Checking if the email address is valid.
# Checking if the email address is valid using regular expression.
if re.search(r"^.+@.+\.com$", email):
    print("Valid")
else:
    print("Invalid")
