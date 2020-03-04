"""Powerful digit counts: How many n-digit positive integers exist which are also an nth power?"""
import numpy as np
import math

count = 0
for n in range(1,1000):
    smallest_n = math.ceil((10**(n-1))**(1/n))
    biggest_n = 9
    count += biggest_n - smallest_n + 1
    if smallest_n > biggest_n:
        break
print(count)