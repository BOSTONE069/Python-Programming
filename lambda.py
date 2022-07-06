from functools import reduce
import  random


def fahrenheit(T):
    return (float(9) / 5) * T + 32


def celsius(T):
    return (float(5) / 9) * (T - 32)


temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahrenheit, temperatures)
C = map(celsius, F)
temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit))
print(temperatures_in_Fahrenheit)
print(temperatures_in_Celsius)

a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]

k = list(map(lambda x, y, z: x + y + z, a, b, c))

print(k)

# Calculating the sum of the numbers from 1 to 100:
addition = reduce(lambda x, y: x + y, range(1, 101))

print(addition)

# finding the sum of number
number = lambda x, y: x + y

print("Sum :", number(4, 6))

# Determine whether a person can vote and returns true or false
can_vote = lambda age: True if age >= 18 else False

print("Can vote :", can_vote(20))

attack = {
    'quick': (lambda: print("Quick Attack")),
    'power': (lambda: print("Power Attack")),
    'missed': (lambda: print("Missed Attack"))

}

attack['quick']()

attackKey = random.choice(list(attack.keys()))

attack[attackKey]()
