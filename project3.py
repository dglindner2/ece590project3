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

    cycle = None

    for vertex in adjList:
        vertex.dist = math.inf
        vertex.prev = None

    # NOTE THIS COULD BE AN ISSUE
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

# NOTE: OUR CURRENT ERROR IS BECAUSE THIS IF STATEMENT IN LINE 46 IS NEVER TRUE
    for vertex in adjList:
        for neighbor in vertex.neigh:
            if neighbor.dist > vertex.dist + adjMat[vertex.rank][neighbor.rank] + tol:
                # This means that there is a cycle
                cycle = neighbor
                break

    path = []

    if cycle is None:
        return []
    else:
        while cycle.prev is not None:
            path.append(cycle.prev)
            cycle = cycle.prev

    # Reverse list
    path = path[::-1]

    return path

################################################################################

"""
rates2mat
"""
def rates2mat(rates):
    # WHAT DOES THIS FUNCTION NEED TO DO
    # Currently this only returns a copy of the rates matrix.
    return [[R for R in row] for row in rates]
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testRates()