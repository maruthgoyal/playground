from Node import Node
from dijkstraQ import minHeap

def djikstra(graph, sourceIndex, destinationIndex):

    path = set()

    queue = minHeap()

    for i in graph:
        queue.append(i)

    while queue.getLen() > 0:

        smallestDistNode = queue.pop()
        path.union(set(smallestDistNode))

        neighbors = smallestDistNode.getNeighbors()

        for i in xrange(len(neighbors[0])):

            nextNode = neighbors[0][i]
            edgeWeight = neighbors[1][i]

            indexOfNextNode = graph.find(nextNode)

            smallestDistNode.relax(nextNode, edgeWeight, indexOfNextNode)

    return path


def main():

    graph = []
    firstNode = True

    nNodes = input("Please enter the number of nodes in the graph: ")
    print

    for i in xrange(nNodes):

        nodeKey = input("Please enter the key of the Node: ")

        newNode = Node(nodeKey)

        if firstNode == True:

            newNode.setDistFromSrcVertex(0)
            firstNode = False

        graph.append(newNode)

    print

    print "Please enter the edges now. When you're done, just type 'done' "
    print "Enter them as 3 spaced numbers. '4 5 1' indicates there is a path from Node #4 to Node #5 with an edge weight of 1 \n(no path from Node #5 to Node #4) based on the order you entered them"

    print

    while True:

        inp = raw_input()

        if inp != 'done':

            indices = [int(x) for x in inp.split()]
            graph[indices[0]].addNeighbor(indices[1], indices[2])

        else:

            break


if __name__ == '__main__':
    main()
