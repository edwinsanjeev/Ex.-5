# Programmer: Edwin
# Date: 11/25/2021
# Description: Exercise 05 (Triangle)
from math import *


side_a = float(input("Enter side A: "))
side_b = float(input("Enter side B: "))
side_c = float(input("Enter side C: "))
perimeter = side_a + side_b + side_c
print()
semi = perimeter /2
# Heron's Formula
area = sqrt(semi*(semi-side_a)*(semi-side_b)*(semi-side_c))

print(f"The perimeter is {perimeter:,.3f}.")
print()
print(f"The area is {area:,.3f}.")