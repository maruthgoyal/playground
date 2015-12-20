from Node import Node

def dfsVisit(node, dic):

    for neighbor in node.getNeighbors()[0]:

        if neighbor not in dic:

            dic[neighbor] = node
            dfsVisit(neighbor, dic)

def dfs(graph):

    parent = {}

    for node in graph:

        if node not in parent:

            parent[node] = None
            dfsVisit(node)

    return parent

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
