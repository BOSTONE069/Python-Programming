import math

PI = math.pi

#This is requesting the user input
radius = input("Enter the radius of the circle: ")

radius = int(radius)

#This is formula for calculating the PI
area_of_circle = PI * radius * radius

# This is to round the number to three decimal place
area_of_circle = round(area_of_circle, 3)

#This is for printing the output
print(f"The area of a circle is {area_of_circle}")
