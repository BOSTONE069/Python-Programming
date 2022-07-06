try:
    number = int(input("Enter the number: "))
    print(f"The number is {number}")
except ValueError:
    print("The number you have entered is not an integer")