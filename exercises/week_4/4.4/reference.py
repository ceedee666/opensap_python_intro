import random

with open('zahlen.txt', 'w') as f:
    for i in range(1000):
        print(random.randint(500, 10000))
