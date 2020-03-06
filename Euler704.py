"""Factors of Two in Binomial Coefficients
FIXME
Define g(n,m) to be the largest integer k such that 2k divides (nm). For example, (125)=792=23⋅32⋅11, hence g(12,5)=3. 
Then define F(n)=max{g(n,m):0≤m≤n}. F(10)=3 and F(100)=6.

Let S(N) = ∑n=1NF(n). You are given that S(100)=389 and S(107)=203222840.

Find S(1016)."""

from math import factorial as fact

def nCr(n,m):
    return (fact(n)//(fact(m)*fact(n-m)))

def g(n,m):
    a = nCr(n,m)
    res = 0
    while a % 2 == 0:
        a //= 2
        res += 1
    # print(a,res, nCr(n,m))
    return res

def F(n):
    a = {g(n,m) for m in range(n)}
    # print(a)
    # print(a, max(a))
    return max(a)

def S(N):
    return sum(F(n) for n in range(1, N + 1))

print(nCr(12,5))
print(g(12,5))
print(F(10))
print(F(100))
print(S(10000))