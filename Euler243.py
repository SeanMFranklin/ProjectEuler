from math import gcd
target_resilience = 15499/94744

# def gcd(a,b):
#     while(b):
#         a, b = b, a % b
#     return a


def phi(n):
    res = n
    p = 2
    while p**2 <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            res -= res//p
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