# "An Account has a balance, and you can deposit and withdraw money from it."
#
# The first line of the class definition is the class header. It consists of the keyword class, followed by the name of
# the class, followed by a colon
class Account:
    def __init__(self):
        """
        The function __init__() is a special function in Python classes. It is run as soon as an object of a class is
        instantiated. The method is useful to do any initialization you want to do with your object.
        """
        self._balance = 0

    @property
    def balance(self):
        """
        The @property decorator allows us to define properties that we can access like attributes, but that are actually
        methods
        :return: The balance of the account.
        """
        return self._balance

    def deposit(self, amount):
        """
        The deposit function adds the amount to the balance.

        :param amount: The amount of money to deposit
        """
        self._balance += amount

    def withdraw(self, amount):
        """
        Withdraws the given amount from the account and returns it.

        :param amount: The amount of money to withdraw from the account
        """
        self._balance -= amount


def main():
    """
    The main function creates an account, deposits $1000, withdraws $500, and prints the balance.
    """
    account = Account()
    account.deposit(1000)
    account.withdraw(500)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()
