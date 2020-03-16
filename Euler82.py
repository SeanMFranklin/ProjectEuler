""" Path sum: three ways
Find the minimal path sum from the top left to the bottom right 
by only moving right and down in matrix.txt"""
import numpy as np
import csv


board = np.array(list(csv.reader(open('p082_matrix.txt'))), dtype=int)

sorted_board = sorted([i for j in list(board) for i in j])
heuristic = [sum(sorted_board[:i]) for i in range(80)][::-1]


class Path:
    def __init__(self, f=0, path=[], y=0, x=0, nodes_visited=set()):
        self.cost = board[y, x]
        self.f = f + self.cost
        self.path = path + [board[y, x]]
        self.nodes_visited = nodes_visited | {board[y, x]}
        self.h = heuristic[x]
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


def a_star(board, y=0):
    queue = [Path(y=y)]
    explored = set()
    while queue[0].x < 79:
        node = queue.pop(0)
        y, x = node.y, node.x
        if y < 79 and (y + 1, x) not in explored:
            insort(queue, Path(node.f, node.path, node.y + 1, node.x, node.nodes_visited))
            explored.add((y + 1, x))
        if x < 79 and (y, x + 1) not in explored:
            insort(queue, Path(node.f, node.path, node.y, node.x + 1, node.nodes_visited))
            explored.add((y, x + 1))
        if y > 0 and (y - 1, x) not in explored:
            insort(queue, Path(node.f, node.path, node.y - 1, node.x, node.nodes_visited))
            explored.add((y - 1, x))
    return queue[0]


ans = [a_star(board, i) for i in range(80)]
print(f"Answer: {min(ans).f}")
