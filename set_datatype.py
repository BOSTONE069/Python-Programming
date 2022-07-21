students = [
    {"name": "John", "country": "Kenya"},
    {"name": "Rhemney", "country": "Uganda"},
    {"name": "Faith", "country": "Tanzania"},
    {"name": "Liam", "country": "United States"},
    {"name": "John", "country": "Kenya"}
]

countries = set()

# Iterating through the list of dictionaries and adding the country to the set.
for student in students:
    countries.add(student["country"])

# Iterating through the set of countries and printing them out.
for country in sorted(countries):
    print(country)
