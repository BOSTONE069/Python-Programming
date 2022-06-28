# This accepts input from the user
first_number, operator, second_number = input("Enter the calculation: ").split()

# This is for converting the stings into integers
first_number = int(first_number)
second_number = int(second_number)

# This is conditional statement for testing the operators
if operator == "+":
    print("{} + {} = {}".format(first_number, second_number, first_number + second_number))
elif operator == "-":
    print("{} - {} = {}".format(first_number, second_number, first_number - second_number))
elif operator == "*":
    print("{} * {} = {}".format(first_number, second_number, first_number * second_number))
elif operator == "/":
    print("{} / {} = {}".format(first_number, second_number, first_number / second_number))
else:
    print("{} % {} = {}".format(first_number, second_number, first_number % second_number))
