
from collections import deque


class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis

    def get_neighbors(self, v):
        return self.adjac_lis[v]


def heurisitc_function(a, b):
    # Uses manhattan distance to calcuate cost
    x1, y1 = a
    x2, y2 = b

    return abs(x1-x2) + abs(y1-y2)


def a_star_algorithm(grid, start, stop):
    # In this open_lst is a lisy of nodes which have been visited, but who's
    # neighbours haven't all been always inspected, It starts off with the start
    # node
    # And closed_lst is a list of nodes which have been visited
    # and who's neighbors have been always inspected
    open_lst = set([start])
    closed_lst = set([])

    # poo has present distances from start to all other nodes
    # the default value is +infinity
    poo = {}
    poo[start] = 0

    # par contains an adjac mapping of all nodes
    par = {}
    par[start] = start

    while len(open_lst) > 0:
        n = None

        # it will find a node with the lowest value of f() -
        for v in open_lst:
            if n == None or poo[v] + grid.h(v) < poo[n] + grid.h(n):
                n = v

        if n == None:
            print('Path does not exist!')
            return None

        # if the current node is the stop
        # then we start again from start
        if n == stop:
            reconst_path = []

            while par[n] != n:
                reconst_path.append(n)
                n = par[n]

            reconst_path.append(start)

            reconst_path.reverse()

            print('Path found: {}'.format(reconst_path))
            return reconst_path

        # for all the neighbors of the current node do
        for (m, weight) in grid.get_neighbors(n):
          # if the current node is not presentin both open_lst and closed_lst
            # add it to open_lst and note n as it's par
            if m not in open_lst and m not in closed_lst:
                open_lst.add(m)
                par[m] = n
                poo[m] = poo[n] + weight

            # otherwise, check if it's quicker to first visit n, then m
            # and if it is, update par data and poo data
            # and if the node was in the closed_lst, move it to open_lst
            else:
                if poo[m] > poo[n] + weight:
                    poo[m] = poo[n] + weight
                    par[m] = n

                    if m in closed_lst:
                        closed_lst.remove(m)
                        open_lst.add(m)

        # remove n from the open_lst, and add it to closed_lst
        # because all of his neighbors were inspected
        open_lst.remove(n)
        closed_lst.add(n)

    print('Path does not exist!')
    return None
