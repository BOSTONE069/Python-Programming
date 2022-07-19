class Student:
    def __init__(self, name, country, dormitory):
        if not name:
            raise ValueError("Missing Name")
        if country not in ["Kenya", "Uganda", "Tanzania", "Burundi", "Rwanda", "DRC"]:
            raise ValueError("Invalid country")
        self.name = name
        self.country = country
        self.dormitory = dormitory

    def __str__(self):
        return f"{self.name} from {self.country} is in {self.dormitory}"

    def charm(self):
        if self.dormitory == "Ayoki":
            return "😂"
        if self.dormitory == "Okoyo":
            return "😇"
        if self.dormitory == "Ogutu":
            return "😆"


def main():
    student = get_student()
    print(student)
    print("Your emoji is: ")
    print(student.charm())


def get_student():
    name = input("Enter the value of your name here: ")
    country = input("Enter the country: ")
    dormitory = input("Enter the name of the dormitory: ")
    return Student(name, country, dormitory)


if __name__ == "__main__":
    main()