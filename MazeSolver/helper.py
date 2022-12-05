import queue


# to keep track of the blocks of maze
class Grid_Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# each block will have its own position and cost of steps taken
class Node:
    def __init__(self, pos: Grid_Position, cost):
        self.pos = pos
        self.cost = cost

    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        else:
            return False


def heuristic_value(curr_node, dest):
    return abs(curr_node.x - dest.x) + abs(curr_node.y - dest.y)


def A_Star(maze, end, start):
    # Create lists for open nodes and closed nodes
    open1 = queue.PriorityQueue()
    closed = [[False for i in range(len(maze))]
              for j in range(len(maze))]
    closed[start.x][start.y] = True

    # using these cell arrays to get neighbours
    adj_cell_x = [-1, 0, 0, 1]
    adj_cell_y = [0, -1, 1, 0]

    # Create a start node and an goal node
    Start = Node(start, 0)
    goal = Node(end, 0)

    # Add the start node
    open1.put((0, Start))
    cost = 0
    cells = 4

    # Loop until the open list is empty
    while open1:

        # Sort the open list to get the node with the lowest cost first
        # no need cuz priority queue
        # Get the node with the lowest cost

        current = open1.get()  # getting least cost node as open1 is a priority queue
        current_node = current[1]  # getting node in cuurent node
        current_pos = current_node.pos

        # Add the current node to the closed list
        if current_node not in closed:
            closed[current_pos.x][current_pos.y] = True
            cost = cost + 1

        # Check if we have reached the goal, return the path (From Current Node to Start Node By Node.parent)
        if current_pos.x == end.x and current_pos.y == end.y:
            print("Algorithm used = A* Algorithm")
            print("No. of moves utilized = ", cost)
            return current_node.cost

        x_pos = current_pos.x
        y_pos = current_pos.y

        # Get neighbours
        for i in range(cells):
            if x_pos == len(maze) - 1 and adj_cell_x[i] == 1:
                x_pos = current_pos.x
                y_pos = current_pos.y + adj_cell_y[i]
                post = Grid_Position(x_pos, y_pos)
            if y_pos == 0 and adj_cell_y[i] == -1:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y
                post = Grid_Position(x_pos, y_pos)
            else:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y + adj_cell_y[i]
                post = Grid_Position(x_pos, y_pos)
            if x_pos < 20 and y_pos < 20 and x_pos >= 0 and y_pos >= 0:
                if maze[x_pos][y_pos] == 1:
                    if not closed[x_pos][y_pos]:
                        neighbor = Node(Grid_Position(
                            x_pos, y_pos), current_node.cost + 1)
                        # get heuristic value of neighbours
                        h = heuristic_value(neighbor.pos, end)
                        f = h + neighbor.cost  # getting f by f = h + g
                        # adding neighbour to closed
                        closed[x_pos][y_pos] = True
                        open1.put((f, neighbor))

    return -1
