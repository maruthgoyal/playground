class minHeap:

    """ A Heap implementation which maintains the min-heap property

        Each parent node is less than both of its children. --> The root node is the min

        Provides O(1) _find_min()
    """

    def __init__(self):

        """

        Initialize empty heap as an Array

        Set its size to 0

        Takes O(1) time

        """

        self.heap = [None] # None added for easy indexing into the array in heapify(). Really. This thing can change your life





    def getLen(self):

        """

        Returns number of elements in the heap

        Takes O(1) time

        """

        return (len(self.heap) - 1)





    def append(self, key):

        """
        Adds an element to the heap

        Correct violation of min-heap property if it occurs

        Takes O(log n) time, n being the size of the new heap

        """
        if key != None:

            self.heap.append(key)
            self.heapify(len(self.heap) - 1, self.heap) # Fixing any violation of the heap property that may have been caused by adding a new element

        else:
            raise ValueError("Cannot add None to heap")




    def min(self):

        """
        Returns minimum element of the Heap

        Takes O(1) time.

        Main feature of data structure implementation

        """
        if len(self.heap) == 1:

            raise ValueError("Dude. It's empty")

        return self.heap[1]





    def pop(self):

        """

        Finds and REMOVES the minimum value from the Heap

        Takes O(lg n) time.

        Returns value of the minimum key


        """
        if(len(self.heap) == 1):

            raise ValueError("The heap is empty. Cannot POP anything.")

        self.swap(1, (len(self.heap) - 1), self.heap) # Swapping last element with first to make removal easy.

        popped_value = self.heap.pop() # Remove last element

        self.heapify(1, self.heap) # Fix Heap violation caused by exchanging last element with first

        return popped_value



    def swap(self, index1, index2, arra):

        """

        Given 2 indices, index1 and index2 and an Array A,

        swap() swaps the values at the 2 indices in the Array.

        Checks:
            Whether both indices are within the Array's range.

        """

        if(index1 < len(arra) and index2 < len(arra) and index1 > -1 and index2 > -1):

            temp = arra[index1]
            arra[index1] = arra[index2]
            arra[index2] = temp



    def heapify(self, index, array):

        """
        Given an Array A and an Index i, corrects a SINGLE violation of the MIN-HEAP property

        Assumes left and right are MIN-HEAPS

        Exchanges parent with the smaller node, if smaller node is present, otherwise nothing happens and it exits.

        Recurses on the index of the smaller node if an exchange does happen

        Takes O(h) where h is the height of the heap or O(log n) where n is the size of the heap

        """

        parent = index / 2 # Parent of the node at the current index
        left_child = parent * 2 # left child of the parent
        right_child = left_child + 1 # right child of the parent

        if(index == 1): # Edge case. Above variable assignments don't apply to the first element

            parent = 1
            left_child = 2
            right_child = 3

        length = len(array)

        minElementOfSubtree = parent # The parent is set to be the min. For now.

        if(index < length and index > 0): # Checking if index is within range of the heap indices

            #print "PARENT OF ", str(array[index]), " IS ",  str(array[parent])

            if(left_child < len(array)): # Checking left_child is within bounds

                if(right_child >= len(array)): # If right_child is out of bounds, left_child is automatically the smaller one

                    minElementOfSubtree = left_child

                else:

                    if (array[left_child].getDistFromSrcVertex() <= array[right_child].getDistFromSrcVertex()): # If the distance from source to left_child is <= dist from src to right_child

                        minElementOfSubtree = left_child


                    else: # dist from src to right_child < dist from src to left_child
                        minElementOfSubtree = right_child

            if(parent != 0 and array[parent].getDistFromSrcVertex() <= array[minElementOfSubtree].getDistFromSrcVertex()): # Giving the parent Node a shot. If dist is lower than current min, set min to be parent

                minElementOfSubtree = parent




            if(minElementOfSubtree != parent): # Heap property has been violated


                self.swap(minElementOfSubtree, parent, array) # Fixing current violation

                if(parent != 1): # Check for violations in the above tree if there is a tree above  "Started from the bottom, now we here"
                    self.heapify(parent, array)

                self.heapify((minElementOfSubtree * 2), array) # Check for violations in the below tree


    def buildMinHeap(self):

        """
        Heapifies the whole heap.
        """

        index = self.getLen()/2 # since n/2 nodes are leaves
        indices = range(1,(index + 1))
        indices = indices[::-1]

        for i in indices:

            if(self.heap[i].keyHasBeenChangedOrNot() == True):
                self.heapify(i, self.heap) # Heapifying every node.
