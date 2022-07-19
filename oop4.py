class Student:
    def __init__(self, name, country):
        if not name:
            raise ValueError("Missing Name")
        if country not in ["Kenya", "Uganda", "Tanzania", "Burundi", "Rwanda", "DRC"]:
            raise ValueError("Invalid country")
        self.name = name
        self.country = country

    def __str__(self):
        return f"{self.name} from {self.country}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Enter the value of your name here: ")
    country = input("Enter the country: ")
    return Student(name, country)


if __name__ == "__main__":
    main()
