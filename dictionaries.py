students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(students["Ron"])
print(students["Draco"])

for student in students:
    print(student, students[student], sep=", ")

