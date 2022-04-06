def is_prime(candidate):
    for i in range(2, candidate):
        if candidate % i == 0:
            return False
    return True


def prime_list(max_number):
    list_primes = []
    for i in range(2, max_number + 1):
        if is_prime(i):
            list_primes.append(i)
    return list_primes


num = int(input("Up to which number do you want all prime numbers: "))
print(prime_list(num))
