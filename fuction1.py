def my_function(counter=89):
    print("Counter: {}".format(counter))


my_function()

#Ask user for the name
name = input("What is your name? ")

second_name = input("What is your second name? ").strip().title()

# Remove whitespace from names
name = name.strip()

name = name.capitalize()

print("Hello: {}".format(name))
print(f"Hello: {name}")
print("Hello,", name)
print("Hello" + name)

print("Please: {}".format(second_name))


