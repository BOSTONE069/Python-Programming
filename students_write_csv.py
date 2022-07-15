import csv

name = input("What's your name? ")
country = input("What's your country? ")

with open("students_1.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "country"])
    writer.writerow({"name": name, "country": country})
