# Function to calculate the area of a triangle using Heron's formula
import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

area = triangle_area(a, b, c)
print(f"The area of a triangle with sides {a}, {b}, and {c} is {area:.2f}")