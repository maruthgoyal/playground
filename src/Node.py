import sys

class Node:

    def __init__(self, key):

        self.edges = [[], []] # List 1 stores the indices of the Nodes it is connected to. List 2 stores the edge weights for the respective edge
        self.key = key
        self.predecessor = -1

        self.distanceFromSourceVertex = (sys.maxint) - 1 # Special thingy for djikstra purposes

    def addNeighbor(self, neighbor, edgeWeight):

        self.edges[0].append(neighbor)
        self.edges[1].append(edgeWeight)

    def removeNeighbor(self, neighbor):

        index = self.edges[0].index(neighbor)

        del self.edges[0][index]
        del self.edges[1][index]

    def changeKey(self, newKey):

        self.key = newKey

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

    def relax(self, otherNode, edgeWeight, indexOfOtherNode):

        if self.getPredecessor > (otherNode.getPredecessor() + edgeWeight):

            self.setDistFromSrcVertex((otherNode.getPredecessor() + edgeWeight))
            self.setPredecessor(indexOfOtherNode)
