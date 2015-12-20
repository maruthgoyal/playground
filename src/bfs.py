from Node import Node

def bfs(graph):

    source = graph[0]
    nodesOnCurrentLevel = [source]

    levels = {source:0}

    i = 1

    while nodesOnCurrentLevel:

        newNodes = []

        for node in nodesOnCurrentLevel:

            neighborIndex = 0

            for neighbor in node.getNeighbors()[0]:

                edgeWeights = graph[neighbor].getNeighbors()[1]

                if graph[neighbor] not in levels:

                    levels[graph[neighbor]] = i
                    graph[neighbor].setDistFromSrcVertex(i + edgeWeights[neighborIndex])
                    graph[neighbor].setPredecessor(node)

                    newNodes.append(graph[neighbor])

                neighborIndex += 1

        nodesOnCurrentLevel = newNodes

    return levels



def main():

    graph = []

    nNodes = int(raw_input("Enter the number of nodes: "))

    print "First key you enter will be the source vertex"


    for i in xrange(nNodes):

        keyValue = int(raw_input("Enter the nodes' key: "))

        graph.append(Node(keyValue))

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

    print bfs(graph)
if __name__ == '__main__':
    main()
