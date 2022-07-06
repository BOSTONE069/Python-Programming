def main():
    hello()
    name = input("What is your name: ").strip().title()
    hello(name)


def hello(to="Welcome to Python Programming"):
    print("Hello,", to)


main()
