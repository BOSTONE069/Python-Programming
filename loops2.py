def main():
    number = get_number()
    boss(number)


def get_number():
    while True:
        n = int(input("Whats is n: "))
        if n > 0:
            return n


def boss(n):
    for _ in range(n):
        print("BOSTONE")


main()