class Node:

    def __init__(self, key):

        self.edges = [[], []] # List 1 stores the indices of the Nodes it is connected to. List 2 stores the edge weights for the respective edge
        self.key = key
        self.predecessor = -1
        self.indexInGraph = -1

        self.distanceFromSourceVertex = 10**5 # Special thingy for dijkstra purposes
        self.decreasedKeyOrNot = False

    def addNeighbor(self, neighbor, edgeWeight):

        self.edges[0].append(neighbor)
        self.edges[1].append(edgeWeight)

    def removeNeighbor(self, neighbor):

        index = self.edges[0].index(neighbor)

        del self.edges[0][index]
        del self.edges[1][index]

    def changeKey(self, newKey):

        self.key = newKey

    def addToDist(self, addend):

        self.distanceFromSourceVertex += addend

    def getKey(self):
        return self.key

    def getNeighbors(self):

        return self.edges

    def getNeighborIndex(self, index):

        return self.edges.index(index)

    def getPredecessor(self):

        return self.predecessor

    def setPredecessor(self, predecessorIndex):

        self.predecessor = predecessorIndex

    def getDistFromSrcVertex(self):

        return self.distanceFromSourceVertex

    def setDistFromSrcVertex(self, newDistance):

        self.distanceFromSourceVertex = newDistance

    def relax(self, graph, edgeWeight, indexOfOtherNode):

        #print (self.getDistFromSrcVertex() + edgeWeight), (graph[indexOfOtherNode].getDistFromSrcVertex()), self.getKey(), graph[indexOfOtherNode].getKey()

        if ((self.getDistFromSrcVertex() + edgeWeight) < graph[indexOfOtherNode].getDistFromSrcVertex()):

            graph[indexOfOtherNode].setDistFromSrcVertex((self.getDistFromSrcVertex() + edgeWeight))
            graph[indexOfOtherNode].setPredecessor(self.indexInGraph)
            graph[indexOfOtherNode].decreasedKeyOrNot = True

        else:

            graph[indexOfOtherNode].decreasedKeyOrNot = False

    def keyHasBeenChangedOrNot(self):

        return self.decreasedKeyOrNot
