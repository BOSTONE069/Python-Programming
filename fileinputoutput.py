name = input("What is your name? ")

file = open("name.txt", "a")
file.write(f"{name}\n")
file.close()
