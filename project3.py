"""
Math 560
Project 3
Fall 2020

Partner 1: George Lindner (dgl12)
Partner 2: Ezinne Nwankwo (esn11)
Date: October 28, 2020
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""


def detectArbitrage(adjList, adjMat, tol=1e-15):
    # Set initial distances and previous nodes.

    for vertex in adjList:
        vertex.dist = math.inf
        vertex.prev = None

    # Initialize start distance to 0
    # Choose starting node as first node in adjacency list
    adjList[0].dist = 0

    # iterate |V| - 1 times
    for i in range(len(adjList) - 1):
        # iterate over each  vertex in adjacency list
        for vertex in adjList:
            # Check each neighbor of the vertex
            for neighbor in vertex.neigh:
                # only update if new node distance gives better offer
                # meaning the distance is shorter
                if neighbor.dist > vertex.dist + adjMat[vertex.rank][neighbor.rank] + tol:
                    neighbor.dist = vertex.dist + adjMat[vertex.rank][neighbor.rank]
                    neighbor.prev = vertex

    # Run extra iteration to check if any distances changed
    # If the optimal value is changed, this implies that there is a cycle
    # Thus, we note which node is changed. And we start from that node
    # That node is called 'cycle'
    cycle = None
    for vertex in adjList:
        for neighbor in vertex.neigh:
            # This if statement only will be true if a distance is updated!
            if neighbor.dist > vertex.dist + adjMat[vertex.rank][neighbor.rank] + tol:
                # This means that there is a cycle
                neighbor.dist = vertex.dist + adjMat[vertex.rank][neighbor.rank]
                neighbor.prev = vertex
                cycle = neighbor
                break
        # As soon as the cycle is not empty, meaning a node was updated, indicating arbitrage
        if cycle is not None:
            break

    # If cycle is none, then no arbitrage and return empty list
    if cycle is None:
        return []
    # If cycle is not none, then we need to traceback the cycle of nodes that had arbitrage
    path = []
    # While the current vertex is not already in the path
    # append the previous nodes to path
    # this returns list of the nodes that were updated after extra iteration
    while cycle.rank not in path:
        path.append(cycle.rank)
        cycle = cycle.prev

    # Now we need to work back to get actual arbitrage cycle
    # and remove any extra nodes not in arbitrage cycle
    cycle = cycle.prev
    path = []
    while cycle.rank not in path:
        path.append(cycle.rank)
        cycle = cycle.prev

    path.append(cycle.rank)

    return path[::-1]


################################################################################

"""
rates2mat
"""


def rates2mat(rates):
    # Currently this only returns a copy of the rates matrix.
    return [[-math.log(R) for R in row] for row in rates]
    ##### Your implementation goes here. #####


"""
Main function.
"""
if __name__ == "__main__":
    testRates()
