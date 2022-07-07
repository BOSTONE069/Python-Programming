students = [
    {"name": "Kevin", "house": "Nairobi", "patronus": "Otter"},
    {"name": "Harry", "house": "Kisumu", "patronus": "Stag"},
    {"name": "Bostone", "house": "Mombasa", "patronus": "Jack Russel"},
    {"name": "Levy", "house": "Nakuru", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
