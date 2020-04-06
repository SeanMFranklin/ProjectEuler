"""Factors of Two in Binomial Coefficients
FIXME: way way too slow
Define g(n,m) to be the largest integer k such that 2k divides (nm). For example, (125)=792=23⋅32⋅11, hence g(12,5)=3. 
Then define F(n)=max{g(n,m):0≤m≤n}. F(10)=3 and F(100)=6.

Let S(N) = ∑n=1NF(n). You are given that S(100)=389 and S(107)=203222840.

Find S(1016)."""

from math import factorial as fact
import Euler
from functools import reduce
import operator as op

g_set = {}
nCr_set = {}

def nCr(n, r):
    if (n,r) in nCr_set:
        return nCr_set[(n,r)]
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    res = numer // denom
    nCr_set[(n,r)] = res
    return res

def g(n,m):
    if (n,m) in g_set:
        return g_set[(n,m)]
    a = nCr(n,m)
    res = 0
    while a % 2 == 0:
        a //= 2
        res += 1
    g_set[(n,m)] = res
    return res

def F(n):
    a = {g(n,m) for m in range(n)}
    return max(a)

def S(N):
    return sum(F(n) for n in range(1, N + 1))

print(S(100))
print(nCr_set)