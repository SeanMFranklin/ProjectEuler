"""Find the minimum spanning tree"""
import numpy as np
import pandas as pd


def find_min_idx(x):
    k = x.argmin()
    ncol = x.shape[1]
    return (k//ncol, k%ncol)

def has_no_cycles(m):
    start = find_min_idx(m)
    queue = [start]
    queue.append((start[1], start[0]))
    visited = []
    while queue:
        node, prev_node = queue.pop()
        for i in m[node]:
            if
        


df = pd.read_csv('p107_network.txt', header=None)
df[df == '-'] = df.max().max()
df = df.astype(int)
df = df.to_numpy()
res = np.zeros_like(df)
print(find_min_idx(df))
print(df)

res = np.zeros_like(df)
