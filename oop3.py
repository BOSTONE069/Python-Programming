class Student:
    def __init__(self, name, country):
        if not name:
            raise ValueError("Missing Name")
        if country not in ["Kenya", "Uganda", "Tanzania", "Burundi", "Rwanda", "DRC"]:
            raise ValueError("Invalid country")
        self.name = name
        self.country = country


def main():
    student = get_student()
    print(f"{student.name} from {student.country}")


def get_student():
    name = input("Enter the value of your name here: ")
    country = input("Enter the country: ")
    return Student(name, country)


if __name__ == "__main__":
    main()
