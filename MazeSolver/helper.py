import pygame
from pygame import Rect, Surface
import random


class Node:
    def __init__(self, pos, *, parent, cost=0) -> None:
        self.pos = pos
        self.parent = parent
        self.cost = cost  # Cost to reach this node
    
    def get_neighbors(self, grid):
        m, n = len(grid), len(grid[0])
        x, y = (0, 1)
        neighbors = []
        if x + 1 < m and grid[x + 1][y] != "WALL":
            neighbors.append((x + 1, y))
        if x - 1 >= 0 and grid[x - 1][y] != "WALL":
            neighbors.append((x - 1, y))
        if y + 1 < n and grid[x][y + 1] != "WALL":
            neighbors.append((x, y + 1))
        if y - 1 >= 0 and grid[x][y - 1] != "WALL":
            neighbors.append((x, y - 1))
        return neighbors



def heuristic_function(pos, GOAL_POS):
    'Uses Manhattan Distance'
    cost = abs(pos[0]- GOAL_POS[0]) + abs(pos[1]- GOAL_POS[1])
    print(
        f"POS:<{pos[0], pos[1]}> | GOAL_POS: <{GOAL_POS[0]}, {GOAL_POS[1]}> | COST: {cost}")
    return cost


def DFS_random(grid, START_POS, GOAL_POS):
    stack = [
        Node(START_POS, parent=None, cost=0)
    ]
    path = []

    visited = set()
    while len(stack) > 0:
        cur = stack.pop()
        visited.add(cur.pos)
        if cur.pos == GOAL_POS:
            tmp = cur
            while tmp.parent is not None:
                path.append(tmp.pos)
                tmp = tmp.parent
            print(path[1:], len(visited))
            #return path[1:], len(visited)
        neighbors = cur.get_neighbors(grid)
        

        # Select neighbor randomly (Random)
        random.shuffle(neighbors)

        for n in neighbors:
            if n not in visited:
                stack.append(Node(n, parent=cur, cost=cur.cost + 1))
    return None



def A_star(grid, START_POS, GOAL_POS):
    priority_queue = [
        Node(START_POS, parent=None, cost=0)
    ]
    path = []    
    visited = set()
    while len(priority_queue) > 0:
        
        # Sort the queue, so that nodes which are closer heuristically are popped first
        # Total Cost for a node X = Heuristic Cost from X to Goal + Cost to reach X
        priority_queue.sort(key=lambda x: heuristic_function(x.pos, GOAL_POS) + x.cost, reverse=True)
        cur = priority_queue.pop()
        visited.add(cur.pos)
        if cur.pos == GOAL_POS:
            tmp = cur
            while tmp.parent is not None:
                path.append(tmp.pos)
                tmp = tmp.parent
            return path[1:], len(visited)
        neighbors = cur.get_neighbors(grid)
        

        for n in neighbors:
            if n not in visited:
                priority_queue.append(Node(n, parent=cur, cost=cur.cost + 1))
    return None
