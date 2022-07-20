class Student:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f"{self.name} from {self.country}"

    @classmethod
    def get(cls):
        name = input("Enter the value of your name here: ")
        country = input("Enter the country: ")
        return cls(name, country)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
