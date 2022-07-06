students = ["Kevin", "Omondi", "Bostone", "Rhemney"]

print(students[1])
print(students[0])

for student in students:
    print(student)

print(f"The student number three is {students[2]}")

for i in range(len(students)):

    print(students[i])

    print(i+1, students[i])

for i in students:
    print("{} : {}".format(students.index(i), i))

#This is for adding elements into the list
students.append("Ochieng")

for i in students:
    print("{} : {}".format(students.index(i), i))

# This is for printing numbers in a list a number of times
print(students[0] * 2)

# This is for changing elements in a list
students[0] = "Melvin"

# This is for sorting the list
students.sort()

for i in students:
    print("{} : {}".format(students.index(i), i))

# List comprehension
evenList = [i * 2 for i in range(10)]

for i in evenList:
    print(i)
