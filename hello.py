print("Hello, world")
name = input("What is your name: ")

#Remove whitespace from string and capitalize users name
name = name.strip().title()

print("Hello, " + name)
print("Hello,", name)
print("Welcome to CS50 {}".format(name))
print(f"Welcome to CS50 {name}")
print("hello,", end="")
print(name)
print("\"Hello\"")
