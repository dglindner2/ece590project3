"""
Math 560
Project 3
Fall 2020

Partner 1:
Partner 2:
Date:
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    ##### Your implementation goes here. #####
    # Set initial dist and prev.

    for vertex in adjList:
        vertex.dist = math.inf
        vertex.prev = None

    # Initialize start distance
    adjList[0].dist = 0

    # iterate |V| - 1 times
    for i in range(len(adjList) - 1):
        for vertex in adjList:
            # Check each neighbor of the vertex
            for neighbor in vertex.neigh:
                # only update if new value is better
                if neighbor.dist > vertex.dist + adjMat[vertex.rank][neighbor.rank] + tol:
                    neighbor.dist = vertex.dist + adjMat[vertex.rank][neighbor.rank]
                    neighbor.prev = vertex


    # This is our extra iteration.
    cycle = None
    for vertex in adjList:
        for neighbor in vertex.neigh:
            # If the optimal value is changed, this implies that there is a cycle.
            # Thus, we note which node is changed. And we start from that node.
            # That node is called 'cycle' in our code
            # This if statement only will be true if a distance is updated!
            if neighbor.dist > vertex.dist + adjMat[vertex.rank][neighbor.rank] + tol:
                # This means that there is a cycle
                neighbor.dist = vertex.dist + adjMat[vertex.rank][neighbor.rank]
                neighbor.prev = vertex
                cycle = neighbor


        if cycle is not None:
            break


    path = []

    # While the current vertex is not already in the path
    while cycle.rank not in path:
        path.append(cycle.rank)
        cycle = cycle.prev

    # BS hack to get the right path
    path.remove(path[0])
    path.append(path[0])

    print(path)
    # we have:    [0, 3, 1, 0]
    # His answer: [0, 3, 1, 0]

    return path

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