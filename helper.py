"""
    Define a class node which used to represent a node/vertices on a graph
    In a maze, each empty square is represented as node
    Add a get_neighbors function to calcuate neighbors for each node.
"""


class Node:
    def __init__(self, pos, *, parent, cost=0) -> None:
        self.pos = pos
        self.parent = parent
        self.cost = cost  # Cost to reach this node

    def get_neighbors(self, grid):
        m, n = len(grid), len(grid[0])
        x, y = self.pos
        neighbors = []

        """
            If statements to check for neighbors in every direction. Left, right, up, down
            Walls are not counted as neighbors, therefore it is != 'WAll'
            Append neighbors to the list and return them.
        """
        if x + 1 < m and grid[x + 1][y] != 'WALL':
            neighbors.append((x + 1, y))
        if x - 1 >= 0 and grid[x - 1][y] != 'WALL':
            neighbors.append((x - 1, y))
        if y + 1 < n and grid[x][y + 1] != 'WALL':
            neighbors.append((x, y + 1))
        if y - 1 >= 0 and grid[x][y - 1] != 'WALL':
            neighbors.append((x, y - 1))
        return neighbors


def heuristic_function(pos, GOAL_POS):
    """ Uses Manhattan Distance 
        It is the distance between two points which is the length of the shortest path that connects them
    """
    cost = abs(pos[0] - GOAL_POS[0]) + abs(pos[1] - GOAL_POS[1])
    return cost


def A_star(grid, START_POS, GOAL_POS):
    """
        Initalize a priority queue to sort all the heuristic values
        In priority queue, elements are served on the basis of their priority.
        That is, higher priority elements are served first.
    """
    priority_queue = [
        Node(START_POS, parent=None, cost=0)
    ]
    'make a list to store the path'
    path = []

    'make a set which will add the visited nodes to it'
    visited = set()
    while len(priority_queue) > 0:

        """
            Sort the queue, so that nodes which are closer heuristically are popped first
            Total Cost for a node is f(n) = g(n) + h(n)
            f(n)= total estimated cost of path through node n
            g(n) = cost so far to reach node n
            h(n) = estimated cost from n to goal. This is the heuristic part of the cost function, so it is like a guess.

        """
        priority_queue.sort(key=lambda x: heuristic_function(
            x.pos, GOAL_POS) + x.cost, reverse=True)

        """pop the heuristic value and add them to visited set."""
        cur = priority_queue.pop()
        visited.add(cur.pos)
        """ if you found the end goal, then program will construct the path """
        if cur.pos == GOAL_POS:
            tmp = cur
            'while the parents exist'
            while tmp.parent is not None:
                'add all the nodes we found to the path'
                path.append(tmp.pos)
                tmp = tmp.parent
            'return the path by slicing it'
            return path[1:]

        """
            calls the get_neighbors function from above
            it will calculate each neighbor from the current node it is at.
        """
        neighbors = cur.get_neighbors(grid)

        'for loop to traverse through not visited neighbors and add them to the queue'
        for n in neighbors:
            if n not in visited:
                priority_queue.append(Node(n, parent=cur, cost=cur.cost + 1))
    return None


'''
def DFS(grid, START_POS, GOAL_POS):
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
            return path[1:]
        neighbors = cur.get_neighbors(grid)
        

        # Select neighbor randomly (Random)
        random.shuffle(neighbors)

        for n in neighbors:
            if n not in visited:
                stack.append(Node(n, parent=cur, cost=cur.cost + 1))
    return None
'''
