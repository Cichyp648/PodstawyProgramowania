###
# Calculation of circle area and circumference 
#
import math 
radius = int(input("Value of r: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f'For the given circle, area = {area:.2f}, and circumference = {circumference:.2f}')