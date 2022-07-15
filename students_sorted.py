students = []

with open("students.csv") as file:
    for line in file:
        name, country = line.rstrip().split(",")
        student = {"name": name, "country": country}
        students.append(student)


def get_names(student):
    return student["name"]


for student in sorted(students, key=get_names):
    print(f"{student['name']} is from {student['country']}")
