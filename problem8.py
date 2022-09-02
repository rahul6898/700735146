# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# “The area of a circle with radius 10 is 314 meters square.”

radius = 10
area = 3.14 * radius ** 2

result = "The area of a circle with radius {radius} is {area} meters square.".format(radius = radius, area = int(area))

print(result)