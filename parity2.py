def main():
    number = int(input("Enter the number: "))
    if is_even(number):
        print("This is an EVEN number")
    else:
        print("This is an ODD number")


# This is using a boolean expression in the functions
def is_even(n):
    return n % 2 == 0


main()
