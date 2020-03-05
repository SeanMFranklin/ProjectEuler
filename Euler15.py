"""Lattice paths
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?"""

"""Imagine possible paths as ddrr, drdr, drrd, rdrd, rrdd, rddr, they are all combinations of 'rrdd'"""
from math import factorial as fact

def nCr(n,m):
    return int(fact(n)/(fact(m)*fact(n-m)))

print(nCr(40,20))