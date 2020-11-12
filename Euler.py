"""
get_prime_factors(n, primes)
prime_sieve(n)
prime_list(n)
get_unique_prime_factors(n, primes)
phi(n)
"""
from math import prod, factorial

def get_prime_factors(n, primes=None):
    """Returns list of prime factors of n"""
    res = []
    if primes:
        i = 0
        while primes[i] <= n**.5:
            if n % primes[i] == 0:
                n //= primes[i]
                res.append(primes[i])
            else:
                i += 1
        res.append(int(n))
    else:
        i = 2
        while i <= n**.5:
            if n % i == 0:
                n //= i
                res.append(i)
            else:
                i += 1
        res.append(int(n))
    return res


def prime_sieve(n):
    """Returns a list of true/false values representing primes up to n"""
    res = [True] * n
    res[0], res[1] = False, False
    for (i, prime) in enumerate(res):
        if prime:
            for j in range(i*i, n, i):
                res[j] = False
    return res


def prime_list(n):
    """Returns a list of primes up to n"""
    is_prime = prime_sieve(n)
    primes = [i for i in range(len(is_prime)) if is_prime[i]]
    return primes


def get_unique_prime_factors(n, primes):
    """Returns a set of unique prime factors of n"""
    res = set()
    i = 0
    while primes[i] <= n**.5:
        if n % primes[i] == 0:
            n //= primes[i]
            res.add(primes[i])
        else:
            i += 1
    res.add(n)
    return res


def phi(n):
    """Returns totient(n)"""
    return n * prod((1 - 1/i for i in get_unique_prime_factors(n)))


def nCr(n, r):
    """Returns n choose r"""
    return int(factorial(n)/(factorial(r)*factorial(n-r)))

def is_prime(n):
    """Returns T/F, whether n is prime or not"""
    if n & 1 == 0:
        return False
    d = 3
    while d ** 2 <= n:
        if n % d == 0:
            return False
        d += 2
    return True
