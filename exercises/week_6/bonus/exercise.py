import random
import math

count = 0
hit = 0

for i in range(100000):
    x = random.random()
    y = random.random()
    if x ** 2 + y ** 2 < 1:
        hit += 1
    count += 1
    if i % 10000 == 0:
        print(4 * hit / count - math.pi)