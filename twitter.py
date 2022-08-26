import re

url = input("URL: ").strip()

# Using a regular expression to remove the beginning of the URL.
username = re.sub("^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

