from Node import Node

def constructPaths(graph):

    """
    Args --> graph, a list of Node objects

    Returns --> A list of lists. Each list consists of a list of indices of the nodes to be followed along the path

    """

    paths = [ [] for x in xrange(len(graph)) ] # Initialise our list

    for i in xrange(len(graph)): # Iterate over all nodes

        index = i # Will be used to repeatedly get the predecessor

        # Setting up the initial values
        paths[i].append(i)

        while True:

            indexOfPred = graph[index].getPredecessor() # Getting the index of the predecessor of this node

            if indexOfPred == -1: # If it is the source vertex, break. (Will break if the current Node doesn't have a predecessor as well)

                break

            else:

                paths[i].append(indexOfPred) # Add the index of the predecessor to our path

                index = indexOfPred # Set index to be the index of the predecessor to repeatedly get predecessors

    return paths

def bfs(graph):

    source = graph[0]
    nodesOnCurrentLevel = [0]

    levels = {0:0}

    currentLevel = 1

    while nodesOnCurrentLevel:

        newNodes = []

        for j in xrange(len(nodesOnCurrentLevel)):

            currentNode = graph[nodesOnCurrentLevel[j]]
            neighbors = currentNode.getNeighbors()[0]

            for k in xrange(len(neighbors)):

                if neighbors[k] not in levels:

                    levels[neighbors[k]] = currentLevel
                    graph[neighbors[k]].setPredecessor(j)
                    print j
                    newNodes.append(k)

        nodesOnCurrentLevel = newNodes

    return levels




def main():

    graph = []

    nNodes = int(raw_input("Enter the number of nodes: "))

    print "First key you enter will be the source vertex"


    for i in xrange(nNodes):

        keyValue = int(raw_input("Enter the nodes' key: "))

        graph.append(Node(keyValue))
        graph[len(graph) - 1].indexInGraph = i

        if len(graph) == 1:
            graph[0].setDistFromSrcVertex(0)

    print
    print "Please enter the edges now. When you're done, just type 'done' "
    print "Enter them as 3 spaced numbers. '4 5 1' indicates there is a path from Node #4 to Node #5 with an edge weight of 1 \n(no path from Node #5 to Node #4) based on the order you entered them"
    print

    while True:

        inp = raw_input()

        if inp != 'done':

            indices = [int(x) for x in inp.split()]
            graph[indices[0] - 1].addNeighbor((indices[1] - 1), indices[2])

        else:

            break
    bfs(graph)
    print constructPaths(graph)
if __name__ == '__main__':
    main()
