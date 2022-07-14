name = input("What is your name? ")

file = open("students.csv", "a")
file.write(f"{name}\n")
file.close()
