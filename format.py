import re

name = input("What is your name? ").strip()
matches = re.search("^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"Hello, {name}")
