import random


class Name:
    country = ["Kenya", "Uganda", "Tanzania", "Burundi", "Rwanda", "DRC"]

    @classmethod
    def sort(cls, name):
        country = random.choice(cls.country)
        print(name, "is in", "{}".format(country))


Name.sort("Bostone")
