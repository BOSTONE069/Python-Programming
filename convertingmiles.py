# This is to ask the user for the input value of miles
mile = input("Enter the value for miles: ")

# This is for converting the string value of miles into integer
mile = int(mile)

# This is the formula for converting the miles into kilometers
kilometers = mile * 1.60934

# This is for printing the value of kilometers using the string format
print("{} Miles equal {:.2f} kilometers".format(mile, kilometers))
