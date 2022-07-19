class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.country}")


def get_student():
    name = input("Enter the value of your name here: ")
    country = input("Enter the country: ")
    student = Student(name, country)
    return student


if __name__ == "__main__":
    main()
