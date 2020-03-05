"""
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from collections import defaultdict
from math import prod


def get_prime_factors(n):
    """Returns list of prime factors of n"""
    res = []
    i = 2
    while i <= int(n**.5):
        if n % i == 0:
            res.append(i)
            n /= i
        else:
            i += 1
    res.append(int(n))
    return res


s = defaultdict(int)
for i in range(2, 21):
    pf = get_prime_factors(i)
    for unique_prime in set(pf):
        s[unique_prime] = max(s[unique_prime], pf.count(unique_prime))
res = 1
for i in s:
    res *= i**s[i]
print(res)
