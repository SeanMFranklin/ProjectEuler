"""
Totient permutation
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum."""
from math import prod


def prime_sieve(n):
    res = [True] * n
    res[0], res[1] = False, False
    for (i, prime) in enumerate(res):
        if prime:
            for j in range(i*i, n, i):
                res[j] = False
    return res

is_prime = prime_sieve(int(1000000))
primes = [i for i in range(len(is_prime)) if is_prime[i]]


def get_unique_prime_factors(n):
    res = set()
    i = 0
    while primes[i] <= int(n**.5):
        if n % primes[i] == 0:
            n //= primes[i]
            res.add(primes[i])
        else:
            i += 1
    res.add(n)
    return res


def phi(n):
    return int(n * prod((1 - 1/i for i in get_unique_prime_factors(n))))


print(989537, phi(989537))
mn = (1e7, 0)
for i in range(2, 10**7):
    if i % 10000 == 0:
        print(f"\r{i/ 100000}%", end='')
    totient_i = phi(i)
    if sorted(str(i)) == sorted(str(totient_i)):
        if i/totient_i < mn[0]:
            mn = (i/totient_i, i)
            # print(mn)
print(mn)
