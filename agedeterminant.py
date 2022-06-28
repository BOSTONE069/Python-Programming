age = eval(input("Enter your age here: "))

if age <= 5:
    print("Go to kindergarten")
elif (age >= 6) and (age <= 17):
    print("Go to grade 1 through 12")
elif age > 17:
    print("Go to college")
else:
    print("Just relax")
