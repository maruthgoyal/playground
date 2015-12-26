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
