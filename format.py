name = input("What is your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{name} {last}"

print(f"Hello, {name}")
