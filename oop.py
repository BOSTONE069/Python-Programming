def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Enter your name: ")
    country = input("Enter your country: ")
    return name, country


if __name__ == "__main__":
    main()
