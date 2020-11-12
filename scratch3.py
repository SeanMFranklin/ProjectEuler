class Path:
    n_nodes = 0

    def __init__(self, f=-1, path=[], xy=(0, 0), nodes_visited=set(), goal=(0, 0)):
        self.x, self.y = xy
        self.cost = 1
        self.f = f + self.cost
        self.goal = goal
        self.path = path + [xy]
        self.nodes_visited = nodes_visited | {xy}
        self.h = self.heuristic(self.x, self.y)
        self.f_plus_h = self.f + self.h
        Path.n_nodes += 1

    def heuristic(self, x, y):
        x_dist = abs(self.goal[0] - x)
        y_dist = abs(self.goal[1] - y)
        return max(x_dist, y_dist) / 2

    def __gt__(self, other):
        return self.f + self.h > other.f + other.h

    def __lt__(self, other):
        return self.f + self.h < other.f + other.h


def insort(queue, node):
    i = 0
    while i < len(queue) and queue[i] < node:
        i += 1
    queue.insert(i, node)


def attack(start, dest, obstacles):
    queue = [Path(goal=dest, xy=start)]
    explored = set()
    explored.add(start)
    explored = explored | set(obstacles)
    visited = {start:0}
    while queue[0].x != dest[0] or queue[0].y != dest[1]:
        node = queue.pop(0)
        y, x = node.y, node.x
        next = [(x+2, y+1), (x+2, y-1), (x+1, y+2), (x+1, y-2),
                (x-1, y+2), (x-1, y-2), (x-2, y+1), (x-2, y-1)]
        for n in next:
            if n not in explored:
                insort(queue, Path(node.f, node.path, n, node.nodes_visited, dest))
                explored.add(n)
        if len(queue) == 0:
            return None
    return queue[0].f




print(attack((0,0), (7,7), ((5,6),(5,8),(6,5),(6,9),(9,6),(8,5),(8,9),(9,8))))
