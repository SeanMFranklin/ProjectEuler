"""
FIXME
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?"""

import Euler
import bisect
from collections import defaultdict

def bisect(iter, num):
    i = 0
    for i, val in enumerate(iter):
        if val > num:
            return i

primes = Euler.prime_list(10000)
# print(primes[0:4])
# a = [1,2,3, 4,5,6]
# print(a[:bisect(a,3)])
d = {0:1}
def f(n, end=len(primes)):
    if n in d:
        return d[n]
    end = min(bisect(primes, n), end)
    # print(n, primes[:end])
    res = 0
    for p in primes[:end]:
        end2 = min(bisect(primes, p), end)
        res += f(n-p, end2)
    d[n] = res
    return res
print(f(5))
print(d)
# res = defaultdict(int)
# res[2] = 1
# a = max(res.values())
# i = bisect(primes, a)
# while a < 5000:
#     for key in res.keys():
#         for p in primes[:i]:
#             res[key + p] += 1


