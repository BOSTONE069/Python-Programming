def main():
    name, country = get_student()
    print(f"{name} from {country}")


def get_student():
    name = input("Enter your name: ")
    country = input("Enter your country: ")
    return name, country


if __name__ == "__main__":
    main()
