class Student:
    country = None
    name = None
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.country}")


def get_student():
    student = Student
    student.name = input("Enter your name: ")
    student.country = input("Enter your country: ")
    return student


if __name__ == "__main__":
    main()
