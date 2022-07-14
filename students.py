with open("students.csv") as file:
    for line in sorted(file):
        name, country = line.rstrip().split(",")
        print(f"{name} is in {country}")