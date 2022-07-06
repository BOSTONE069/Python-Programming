from functools import reduce


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
