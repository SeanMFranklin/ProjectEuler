"""We define the Matrix Sum of a matrix as the maximum sum of matrix elements with each element being the only one in his row and column. 
For example, the Matrix Sum of the matrix below equals 3315 ( = 863 + 383 + 343 + 959 + 767):

  7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943
767 473 103 699 303

Find the Matrix Sum of:"""

import numpy as np
from random import shuffle
nums = np.array([[int(i) for i in j.split()] for j in open('p345_matrix.txt')])
pos = [i for i in range(len(nums))]
n = len(nums)

running_max = 0
for k in range(100):
    shuffle(pos)
    progress = True
    while progress:
        progress = False
        for i in range(n):
            for j in range(i):
                if nums[pos[j], i] + nums[pos[i], j] > nums[pos[i], i] + nums[pos[j], j]:
                    pos[i], pos[j] = pos[j], pos[i]
                    progress = True
    res = 0
    for i in range(n):
        res += nums[pos[i], i]
    running_max = max(running_max, res)

print(running_max)
