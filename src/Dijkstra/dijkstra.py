from Node import Node # A class to provide fields and methods to our Nodes
from dijkstraQ import minHeap # Our Priority queue

def constructPaths(graph):

    """
    Args --> graph, a list of Node objects

    Returns --> A list of lists of lists. Each list consists of a list of indices of the nodes to be followed along the path and the length of the path

    Given a dijkstra-processed graph, returns the shortest paths from the source vertex to a node and the length of the path

    We assume distance cannot be greater than 10^5 for simplicity. (Based on the relax() method of the Node class. If it's greater, it hasn't been relaxed, hence it isn't reachable)
    Sets distance to be -1 if Node is unreachable from src
    """

    paths = [ [[], -1] for x in xrange(len(graph)) ] # Initialise our list

    for i in xrange(len(graph)): # Iterate over all nodes

        index = i # Will be used to repeatedly get the predecessor
        dist = graph[i].getDistFromSrcVertex() # Distance of the Node from the source vertex

        if dist > (10**5): # Node is unreachable from src
            dist = -1

        # Setting up the initial values
        paths[i][1] = dist
        paths[i][0].append(i)

        while True:

            indexOfPred = graph[index].getPredecessor() # Getting the index of the predecessor of this node

            if indexOfPred == -1: # If it is the source vertex, break. (Will break if the current Node doesn't have a predecessor as well)

                break

            else:

                paths[i][0].append(indexOfPred) # Add the index of the predecessor to our path

                index = indexOfPred # Set index to be the index of the predecessor to repeatedly get predecessors

    return paths



def dijkstra(graph):

    """
    Given a graph, computes the shortest path from a single source vertex to every other reachable vertex

    """

    queue = minHeap() # Our Priority queue

    for i in graph: # Adding all nodes to the Priority queue
        queue.append(i)

    while queue.getLen() > 0:

        smallestDistNode = queue.pop() # Getting the Node with minimum distance from src vertex from the Priority queue

        neighbors = smallestDistNode.getNeighbors() # All the neighbors of that node

        for i in xrange(len(neighbors[0])): # Iterating over all neighbors

            edgeWeight = neighbors[1][i] # Edge weight of the edge between smallestDistNode and the ith neighbor
            indexOfNextNode = neighbors[0][i] # index of neighbor

            smallestDistNode.relax(graph, edgeWeight, indexOfNextNode) # relaxing the neighbor. See Node.py for more

        queue.buildMinHeap() # Fixing the min-heaps property since the distanceFromSourceVertex values may have gotten altered during relax()

    constructedPaths = constructPaths(graph) # Generating the paths using the predecessor of each Node

    return constructedPaths


def main():

    graph = []
    firstNode = True

    nNodes = input("Please enter the number of nodes in the graph: ")
    print

    for i in xrange(nNodes):

        nodeKey = input("Please enter the key of the Node: ")

        graph.append(Node(nodeKey)) # creating a new Node with nodeKey as its key and adding it to our graph

        if firstNode == True: # If this is the 1st Node, make it the source vertex by setting its distance from itself to 0

            graph[(len(graph) - 1)].setDistFromSrcVertex(0)
            firstNode = False

        graph[(len(graph) - 1)].addToDist(i) # Adding the index to the initial distance in order to preserve the order of Node processing in the minHeap later on
        graph[(len(graph) - 1)].indexInGraph = i # Setting the index of the node in our graph. Useful in the relax() method

    print

    print "Please enter the edges now. When you're done, just type 'done' "
    print "Enter them as 3 spaced numbers. '4 5 1' indicates there is a path from Node #4 to Node #5 with an edge weight of 1 \n(no path from Node #5 to Node #4) based on the order you entered them"

    print

    while True:

        inp = raw_input()

        if inp != 'done':

            indices = [int(x) for x in inp.split()]
            graph[indices[0] - 1].addNeighbor((indices[1] - 1), indices[2]) # Creating a directed edge from Node #indices[0] - 1 to Node #indices[1] - 1 with an edge weight of indices[2]

        else:

            break

    print dijkstra(graph)


if __name__ == '__main__':
    main()
