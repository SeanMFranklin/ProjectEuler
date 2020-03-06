from math import gcd
target_resilience = 15499/94744

# def gcd(a,b):
#     while(b):
#         a, b = b, a % b
#     return a

def prime_sieve(n):
    res = [True] * n
    res[0], res[1] = False, False
    for (i, prime) in enumerate(res):
        if prime:
            for j in range(i*i, n, i):
                res[j] = False
    return res

is_prime = prime_sieve(int(1000000000 ** .5))
primes = [i for i in range(len(is_prime)) if is_prime[i]]
print(primes)

def phi(n):
    res = n
    p = 0
    while primes[p]**2 <= n:
        if n % primes[p] == 0:
            while n % primes[p] == 0:
                n = n // primes[p]
            res -= res//primes[p]
        p += 1
    if (n > 1):
        res -= res//n
    return res


def resilience(n):
    return phi(n) / (n-1)


for i in range(3, 1000000000):
    if (i) % 100000 == 0:
        print(i)
    if resilience(i) < target_resilience:
        print(i)
        break