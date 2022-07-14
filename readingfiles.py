with open("name.txt", "r") as file:
    lines = file.readlines()

for line in sorted(lines):
    print("Hello,", line, end="")
