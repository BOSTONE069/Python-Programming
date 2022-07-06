# This is for requesting user input
money = input("How much to invest: ")
interest_rate = input("Interest rate: ")

# This is for converting money to float
money = float(money)

# This is for converting a float and round the percentage rate by 2 digits
interest_rate = float(interest_rate) * .01

# This is to cycle through 10 years using a for loop from 0 to 9
for i in range(10):
    money = money + (money * interest_rate)

# This is for output of the results
print("Investment after 10 years: {:.2f}".format(money))
