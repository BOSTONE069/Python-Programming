class Student:
    """
    The __init__ function is called when a new instance of the class is created.
    param name: The name of the city
    :param country: The country the city is in
    """
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f"{self.name} from {self.country}"

    """
    The @classmethod decorator is used to create a 
    method that can be called either on the class (such as C.get()) or on
    an instance (such as C().get())

    :param cls: This is the class object
    :return: The class is being returned.
    """
    @classmethod
    def get(cls):
        name = input("Enter the value of your name here: ")
        country = input("Enter the country: ")
        return cls(name, country)


def main():
    """
    `main()` gets a student from the database and prints it
    """
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
