class Student:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f"{self.name} from {self.country}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        if country not in ["Kenya", "Uganda", "Tanzania", "Burundi", "Rwanda", "DRC"]:
            raise ValueError("Invalid country")
        self._country = country


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Enter the value of your name here: ")
    country = input("Enter the country: ")
    return Student(name, country)


if __name__ == "__main__":
    main()
