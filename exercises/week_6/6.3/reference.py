import random
import statistics


def gaussian_distribution(mean=100, standard_derivation=10):
    return [random.gauss(mean, standard_derivation) for _ in range(1000)]


random_list = gaussian_distribution()
print("Mean: ", statistics.mean(random_list))
print("Standard Deviation: ", statistics.stdev(random_list))
