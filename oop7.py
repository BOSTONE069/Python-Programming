import random


class Name:
    def __init__(self):
        self.country = ["Kenya", "Uganda", "Tanzania", "Burundi", "Rwanda", "DRC"]

    def sort(self, name):
        country = random.choice(self.country)
        print(name, "is in", "{}".format(country))


my_name = Name()
my_name.sort("Bostone")
