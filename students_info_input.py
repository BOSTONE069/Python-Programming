name, country = input("What is your name? ").split()

file = open("students.csv", "a")
file.write(f"{name}, {country}\n")
file.close()
