def main():
    student = get_student()
    print(f"{student['name']} from {student['country']}")


def get_student():
    name = input("Enter your name: ")
    country = input("Enter your country: ")
    return {"name": name, "country": country}


if __name__ == "__main__":
    main()

