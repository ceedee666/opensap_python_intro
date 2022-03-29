def prime(cand):
    p = True
    for i in range(2, cand):
        if cand % i == 0:
            p = False
    return p

def prime_list(num):
    list_primes = []
    for i in range (2, num + 1):
        if prime(i):
            list_primes.append(i)
    return list_primes

num = int(input("Up to which number do you want all prime numbers: "))
print(prime_list(num))