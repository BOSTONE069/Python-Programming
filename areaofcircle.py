import math

PI = math.pi

#This is requesting the user input
radius = input("Enter the radius of the circle: ")

radius = int(radius)

#This is formula for calculating the PI
area_of_circle = PI * radius * radius

# This is to round the number to three decimal place
area_of_circle = round(area_of_circle, 5)

#This is for printing the output
print(f"The area of a circle is {area_of_circle}")

#This is for printing the output in two decimal places
print(f"The are of the circle is {area_of_circle:.2f}")
