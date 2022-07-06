try:
    number = int(input("Enter the number: "))
    print(f"The number is {number}")
except ValueError:
    print("The number you have entered is not an integer")

# using the try with else
try:
    number = int(input("Enter the number: "))
except ValueError:
    print("The number you have entered is not an integer")
else:
    print(f"The number is {number}")

# This is to loop several times
while True:
    try:
        number = int(input("Enter the number: "))
    except ValueError:
        print("The number you have entered is not an integer")
    else:
        break

print(f"The number is {number}")


# This is to loop several times
while True:
    try:
        number = int(input("Enter the number: "))
    except ValueError:
        pass
    else:
        break

print(f"The number is {number}")
