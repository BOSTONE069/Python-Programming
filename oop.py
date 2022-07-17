def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")


def get_name():
    name = input("Enter your name: ")
    return name


def get_house():
    house = input("Enter your house: ")
    return house


if __name__ == "__main__":
    main()
