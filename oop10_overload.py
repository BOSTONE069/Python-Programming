class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        """
        This function takes in three parameters, galleons, sickles, and knuts, and sets the values of the instance variables
        galleons, sickles, and knuts to the values of the parameters galleons, sickles, and knuts.

        :param galleons: The number of galleons in the amount of money, defaults to 0 (optional)
        :param sickles: The number of sickles in the amount of money, defaults to 0 (optional)
        :param knuts: The smallest unit of currency in the wizarding world, defaults to 0 (optional)
        """
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        """
        It takes two objects, adds their galleons, sickles, and knuts, and returns a new Vault object with the sum of the
        galleons, sickles, and knuts

        :param other: The other Vault object that is being added to the current Vault object
        :return: A Vault object
        """
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

wesley = Vault(25, 50, 100)
print(wesley)

total = potter + wesley
print(total)
