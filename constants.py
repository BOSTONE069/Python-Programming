class Cat:
    # A class variable.
    MEOWS = 3

    def meows(self):
        """
        For the number of meows in the class, print 'Meows'.
        """
        for _ in range(self.MEOWS):
            print("Meows")


cat = Cat()
cat.meows()
