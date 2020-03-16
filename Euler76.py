"""It is possible to write five as a sum in exactly six different ways:
TODO

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?"""
import numpy as np
pos = [1 for i in range(101)]
pos[0] = 0
pos = np.array(pos)

for i in range(1,100):
    pos[i+1] += pos[i]

print(pos)