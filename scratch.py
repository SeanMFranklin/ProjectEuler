from time import time
from math import factorial as fact
import operator as op
from functools import reduce

def nCr_fact(n,m):
    return (fact(n)//(fact(m)*fact(n-m)))

def nCr_red(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

start = time()
for i in range(1000):
    nCr_fact(10000,1000)
print(f"nCr_fact took {time()-start} seconds.")

start = time()
for i in range(1000):
    nCr_red(10000,1000)
print(f"nCr_red took {time()-start} seconds.")