import re

url = input("URL: ").strip()

if matches := re.search("^(https?://)?(?:www\.)?twitter\.com/(\w+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(2))
else:
    pass
