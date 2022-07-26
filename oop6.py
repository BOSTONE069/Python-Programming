class Student:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f"{self.name} from {self.country}"

    """
    The @property decorator allows us to define properties that we can access like attributes and that we can also set
    like regular attributes
    :return: The name of the person.
    """

    @property
    def name(self):
        return self._name

    """
    The @name.setter decorator is used to define a setter function for the name attribute
     :param name: The name of the person
     """

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    @property
    def country(self):
        return self._country

    """
    The `@property` decorator allows us to define properties that we can then get and set like attributes
    :param country: The country the user is in
    """

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
