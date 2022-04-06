import math
from random import random

NUMBER_OF_POINTS = 10000
points_inside_circle = 0

points = [(random(), random()) for _ in range(10000)]
inside_points = [p[0] ** 2 + p[1] ** 2 < 1 for p in points]
points_inside_circle = inside_points.count(True)
p = 4 * points_inside_circle / NUMBER_OF_POINTS

print("Calculated value of π:", p)
print("Value of π from math library:", math.pi)
print("Difference:", p - math.pi)
