""" Path sum: four ways
Find the minimal path sum from the top left to the bottom right 
by only moving right and down in matrix.txt"""
import numpy as np
import csv
from matplotlib import pyplot as plt
from collections import defaultdict

board = np.array(list(csv.reader(open('p081_matrix.txt'))), dtype=int)
# board = np.random.randint(1, high=10000, size=(200, 200))
height, width = board.shape
height -= 1
width -= 1

sorted_board = sorted([i for j in list(board) for i in j])
heuristic = [sum(sorted_board[:i]) for i in range(height + width + 2)][::-1]
# print(heuristic)
# heuristic = defaultdict(lambda: 10000)
# for j in range(height):
#     for i in range(width):
#         heuristic[i+j] = min(heuristic[i+j], board[j,i])
# res = [0]
# for i in range(159):
#     res.append(heuristic[i] + res[i])
# heuristic = res[::-1]
# print(heuristic)

class Path:
    def __init__(self, f=0, path=[], y=0, x=0, nodes_visited=set()):
        self.cost = board[y, x]
        self.f = f + self.cost
        self.path = path + [(y, x)]
        self.nodes_visited = nodes_visited | {board[y, x]}
        self.h = heuristic[x+y]
        # self.h = (np.sum(board[y,x:]) + np.sum(board[y:,-1])) // 4
        self.f_plus_h = self.f + self.h
        self.y = y
        self.x = x

    def __gt__(self, other):
        return self.f + self.h > other.f + other.h

    def __lt__(self, other):
        return self.f + self.h < other.f + other.h


def insort(queue, node):
    i = 0
    while i < len(queue) and queue[i] < node:
        i += 1
    queue.insert(i, node)


def a_star(board):
    queue = [Path()]
    explored = set()
    while queue[0].x < width or queue[0].y < height:
        node = queue.pop(0)
        y, x = node.y, node.x
        if y < height and (y + 1, x) not in explored:
            insort(queue, Path(node.f, node.path, node.y + 1, node.x, node.nodes_visited))
            explored.add((y + 1, x))
        if x < width and (y, x + 1) not in explored:
            insort(queue, Path(node.f, node.path, node.y, node.x + 1, node.nodes_visited))
            explored.add((y, x + 1))
        if x > 0 and (y, x - 1) not in explored:
            insort(queue, Path(node.f, node.path, node.y, node.x - 1, node.nodes_visited))
            explored.add((y, x - 1))
        if y > 0 and (y - 1, x) not in explored:
            insort(queue, Path(node.f, node.path, node.y - 1, node.x, node.nodes_visited))
            explored.add((y - 1, x))
    print(len(explored))
    return queue[0]


ans = a_star(board)
print(f"Answer: {ans.f}")

Y = [height - i[0] for i in ans.path]
X = [i[1] for i in ans.path]
plt.plot(X,Y)
plt.show()