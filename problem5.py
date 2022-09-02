#Given the radius of a circle is 30 meters.
#Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
# Calculate the circumference of a circle and assign the value to a variable name of
# _circum_of_circle_
# • Taking radius as user input and calculate the area.


radius = 30
_area_of_circle_ = 3.14 * radius * radius
_circum_of_circle_ = 2 * 3.14 * radius
print(f'area with new radius: {_area_of_circle_}')
print(f'circumference with new radius: {_circum_of_circle_}')


radius = int(input('enter radius: '))
print(f'area with new radius: {3.14 * radius * radius}')