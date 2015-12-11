from Node import Node
from dijkstraQ import minHeap

def constructPaths(graph):

    paths = [ [[], -1] for x in xrange(len(graph)) ]

    for i in xrange(len(graph)):

        index = i
        dist = graph[i].getDistFromSrcVertex()

        paths[i][1] = dist
        paths[i][0].append(i)

        while True:

            indexOfPred = graph[index].getPredecessor()

            if indexOfPred == -1:

                break

            else:

                paths[i][0].append(indexOfPred)

                index = indexOfPred

    return paths



def dijkstra(graph):

    path = set()

    queue = minHeap()

    for i in graph:
        queue.append(i)

    while queue.getLen() > 0:

        smallestDistNode = queue.pop()
        path.union({smallestDistNode})

        neighbors = smallestDistNode.getNeighbors()

        for i in xrange(len(neighbors[0])):

            edgeWeight = neighbors[1][i]
            indexOfNextNode = neighbors[0][i]

            smallestDistNode.relax(graph, edgeWeight, indexOfNextNode)

        queue.buildMinHeap()

        constructedPaths = constructPaths(graph)

    return constructedPaths


def main():

    graph = []
    firstNode = True

    nNodes = input("Please enter the number of nodes in the graph: ")
    print

    for i in xrange(nNodes):

        nodeKey = input("Please enter the key of the Node: ")

        graph.append(Node(nodeKey))

        if firstNode == True:
            graph[(len(graph) - 1)].setDistFromSrcVertex(0)
            firstNode = False

        graph[(len(graph) - 1)].addToDist(i)
        graph[(len(graph) - 1)].indexInGraph = i

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

    print dijkstra(graph)


if __name__ == '__main__':
    main()
