balance = 0


def main():
    """
    It prints the current balance, withdraws $100, deposits $400, and prints the new balance
    """
    print("Balance:", balance)
    withdraw(100)
    deposit(400)
    print("Balance:", balance)


def withdraw(n):
    """
    The withdraw function subtracts the value of n from the global variable balance.

    :param n: the amount to withdraw
    """
    global balance
    balance -= n


def deposit(n):
    """
    The deposit function adds the amount n to the global variable balance.

    :param n: the amount of money to deposit
    """
    global balance
    balance += n


if __name__ == "__main__":
    main()
