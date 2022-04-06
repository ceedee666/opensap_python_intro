import math
import random

NUMBER_OF_POINTS = 10000
points_inside_circle = 0

for i in range(NUMBER_OF_POINTS):
    x = random.random()
    y = random.random()
    if x**2 + y**2 < 1:
        points_inside_circle += 1

pi = 4 * points_inside_circle / NUMBER_OF_POINTS

print("Calculated value of π:", pi)
print("Value of π from math library:", math.pi)
print("Difference:", pi - math.pi)
