email = input("What is your email address? ").strip()

if "@" in email and "." in email:
    print("valid")
else:
    print("invalid")
