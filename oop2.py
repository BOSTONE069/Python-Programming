class Student:
    country = None
    name = None
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.country}")


def get_student():
    """
    It creates a new Student object, sets its name and country attributes, and returns the object
    :return: The student object is being returned.
    """
    # Creating a new Student object.
    student = Student
    student.name = input("Enter your name: ")
    student.country = input("Enter your country: ")
    return student


if __name__ == "__main__":
    main()
