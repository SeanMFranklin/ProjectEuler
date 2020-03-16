""" Path sum: two ways
Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt"""
import numpy as np
import csv
from collections import deque


board = np.array(list(csv.reader(open('p081_matrix.txt'))), dtype=int)
board = board[::-1, ::-1]
for i in range(1, 80):
    board[i, 0] += board[i-1, 0]
    board[0, i] += board[0, i-1]
for i in range(1,80):
    for j in range(1,80):
        board[j,i] += min(board[j-1,i], board[j,i-1])

print(board[79,79])