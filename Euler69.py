"""
Totient maximum
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	1	2
3	1,2	2	1.5
4	1,3	2	2
5	1,2,3,4	4	1.25
6	1,5	2	3
7	1,2,3,4,5,6	6	1.1666...
8	1,3,5,7	4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum."""
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
    return n * prod((1 - 1/i for i in get_unique_prime_factors(n)))


mx = (0, 0)
for i in range(2, 1000000):
    if i % 100000 == 0:
        print(i)
    mx = max(mx, (i/phi(i), i))

print(mx)
