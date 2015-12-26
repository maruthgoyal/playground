"""
This program takes a string as input from the user and outputs a binary string which is created by the Huffman Encoding system applied to that string.

In general:

To get a Huffman tree:

1. Split the string into characters

2. Count the frequency of each character

3. Sort the characters by frequency

4. Take the 2 characters with the least frequency and combine them into a single node.

5. Set the frequency of this node to the sum of the frequency of the two characters which were combined

6. Repeat until the frequency value of the root node does not equal the length of the string


To get the Huffman string:

1. Start at the root node

2. See which child's character list contains your character

3. If you go left, add a '0' to your binary string. '1' if you go right

4. Continue this process on each node you go to (either left or right) till you reach a leaf.

5. The combined string is the Huffman code for that character

6. Repeat this for each character in the string


NOTE: Python was acting crazy in this program. I was using a class-based structure (as you can see).
      However, Python would somehow magically lose the values of huffNode.left and huffNode.right
      as soon as it exited the huffify() method. I checked my code multiple times, to no avail.

      TODO: Check what went wrong.
      UPDATE: Was assigning new object to a single variable. Since variable was being changed, data was being lost. Have to change to annonymous object instances for class-based.

"""

class huffNode(object):

    """

    Usage: my_node = huffNode()

    A single Node in a Huffman Tree.

    Provides the following fields:

    A. List of characters of the node  (To indicate which characters have been combined to form this node)

    B. The index of the right child of the node (Required to traverse the tree)

    C. The index of the left child of the node (Required to traverse the tree)

    D. The key of the node (The total frequency of all the characters combined to make the node)

    Use the respective GET methods to get the value of each field and the SET methods to set the value.


    """

    def __init__(self):

        """

        Usage: You don't.

        Initialize each field of a Huffman Tree's node.

        """

        self.chars = ""   # STRING
        self.right = -2349809834 # INTEGER
        self.left = -2349809834 # INTEGER
        self.key = -1 # INTEGER



    def setKey(self, n):

        """

        Usage: your_node.setKey(key)

        Arguments: n --> The value of the key you want to set

        Sets the nodes key value.

        """

        self.key = n

    def addChar(self, c):

        """

        Usage: your_node.addChar(character)

        Arguments: c --> The character you want to append to the string characters that combine to make this node

        Given a character, adds it to the string of characters that comprise this node.

        """
        if(c not in self.chars):
            self.chars += c

    def setRight(self, r):

        """

        Usage: your_node.setRight(right_child_index)

        Arguments: r --> Index of right child. The index of the node you want to set as the right child of this node

        Given index of another node, sets it to be the right child of this node

        """

        self.right = r

    def setLeft(self, l):

        """

        Usage: your_node.setLeft(left_child_index)

        Arguments: l --> Index of left child. The index of the node you want to set as the left child of this node

        Given index of another node, sets it to be the left child of this node


        """

        self.left = l

    def getChars(self):

        """

        Usage: your_node.getChars()

        Returns: String

        Returns the string of characters which comprise this Node

        """

        return self.chars

    def getLenChars(self):

        """

        Usage: your_node.getLenChars()

        Returns: An integer

        Returns the number of characters that comprise this Node

        """

        return len(self.chars)

    def getLeft(self):

        """

        Usage: your_node.getLeft()

        Returns: Integer

        Returns the index of the left child of this Node

        """

        return self.left

    def getRight(self):

        """

        Usage: your_node.getRight()

        Returns: Integer

        Returns the index of the right child of this Node

        """

        return self.right

    def getKey(self):

        """

        Usage: your_node.getKey()

        Returns: An integer

        Returns the key value of this Node --> Combined frequency of all characters of this node

        """

        return self.key






def getSetupListFromString(string):

    """

    Usage: getSetupListFromString(string)

    Arguments: string --> The string that is to be setup for "huffing"

    Returns: A list

    Given a string, generates a list of ordered pairs of the following format:  [frequency_of_a_character_in_the_string, character]
    No character is repeated.

    """

    dic = {}

    for i in string:

        if i not in dic:
            dic[i] = string.count(i)

    li = [[y,x] for x,y in dic.items()]
    li = sorted(li, reverse=True) # Sorting in descending order

    return li






def huffify(li, y):

    """

    Usage: huffify(list)

    Arguments: li --> A list of the following format: [ [frequency_of_character (integer), character (String)], ...]
                        which has been sorted in descending order by the frequency values.

    Returns: huffNode object instance

    Given a list of ordered pairs [frequency_of_a_character_in_the_string, the_character] generates a Huffman Tree structure using the huffNode class.
    Returns the root node of the tree. Each node has a "left" and "right" field which can be used to traverse the tree.

    """

    root = huffNode()
    nodes = []
    neighbors = {}
    while(root.getKey() != len(y)):

        newNode = huffNode()

        keys = [None, None]
        characters = [None, None]


        for i in xrange(2):

            if len(li) != 0:

                lastEl = li[len(li) - 1]

                keys[i] = lastEl[0]
                characters[i] = lastEl[1]

                li.pop()


            else:

                break

        if(characters[0] == None or characters[1] == None):
            break
        joinedCharacterString = characters[0] + characters[1]

        li.append([sum(keys), joinedCharacterString])

        li = sorted(li, reverse = True)



        left = huffNode()
        left.setKey(keys[0])
        left.addChar(characters[0])


        right = huffNode()
        right.setKey(keys[1])
        right.addChar(characters[1])



        lIndex = -1
        rIndex = -1

        if right.getChars() not in [x.getChars() for x in nodes]:

            nodes.append(right)
            rIndex = len(nodes) - 1

        else:

            rIndex = [x.getChars() for x in nodes].index(right.getChars())

        if left.getChars() not in [x.getChars() for x in nodes]:

            nodes.append(left)
            lIndex = len(nodes) - 1

        else:

            lIndex = [x.getChars() for x in nodes].index(left.getChars())


        for string in characters:

            for character in string:

                newNode.addChar(character)



        newNode.setLeft(lIndex)
        newNode.setRight(rIndex)
        newNode.setKey(sum(keys))

        neighbors[newNode.getChars()] = (lIndex, rIndex)

        root = newNode

    nodes.append(root)

    return (nodes, neighbors)



dictionary = {}


def getHuffBinChar(character, tree):

    """

    Usage: getHuffBinChar(character, huffman_tree)

    Arguments: character --> The character for which the Huffman Encoding is to be generated
                tree --> A pre-generated Huffman Tree (see huffify() for more info)

    Returns: string

    Given a character and a pre-generated Huffman tree, calculates the Huffman Encoding of a single character

    """

    binStr = ""

    (tre,neigh) = (tree[0], tree[1])

    currentIndex = len(tre) - 1
    currentNode = tre[currentIndex]

    while(currentNode.getChars() != character and currentIndex > -1 and currentNode.getChars() != ''):

        if(neigh[currentNode.getChars()][0] < 0 or neigh[currentNode.getChars()][1] < 0):
            break

        else:

            left = tre[neigh[currentNode.getChars()][0]]
            right = tre[neigh[currentNode.getChars()][1]]

            if(left != None or right != None):

                if(character in left.getChars()):

                    binStr += '0'
                    currentIndex = neigh[currentNode.getChars()][0]

                elif(character in right.getChars()):

                    binStr += '1'
                    currentIndex = neigh[currentNode.getChars()][1]

            else:

                raise ValueError("Invalid input. Character is not in string")

            currentNode = tre[currentIndex]


    if(character != '\n'):
        dictionary[binStr] = character

    return binStr






def getHuffBinString(string, tree):

    """

    Usage: getHuffBinString(string, huffman_tree)

    Arguments: string --> The string that is to be encoded
               huffman_tree --> A pre-generated Huffman tree (see huffify() for more info)

    Returns: string

    Given a string and a pre-generated Huffman Tree, returns a binary string encoded using the Huffman Encoding system by calculating it character by character

    """
    a = False
    binStr = ""
    for x in string:
        if x != " ":
            a = True

    if a == True:

        for character in string:

            huffChar = getHuffBinChar(character, tree)
            binStr += (huffChar + " ")

    return binStr






def huffmanEncodedStr(string):

    """

    Usage: huffmanEncodedStr(your_string)

    Arguments: string --> The string that is to be encoded

    Returns: string

    Generates a binary string which is a Huffman Encoding of the given string

    """

    setup_list = getSetupListFromString(string)

    tree = huffify(setup_list, string)

    huffString = getHuffBinString(string, tree)

    return huffString



def getDic():

    return dictionary


def main():

    """

    Usage: main()
    Returns: None

    Main method. Takes a string as input from the user and prints out a binary string enocded using the Huffman Coding system

    """

    inp = raw_input()

    print huffmanEncodedStr(inp)




if __name__ == '__main__':
    main()
