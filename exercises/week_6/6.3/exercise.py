import statistics
import random

mn = 100
sd = 10
random_list = []
for i in range(1000):
    random_list.append(random.gauss(mn, sd))

print("Mean: ", statistics.mean(random_list))
print("StDev: ", statistics.stdev(random_list))