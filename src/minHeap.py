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
        
        self.heap = [None]
        
        
        
        
        
    def __len__(self):
        
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
            self.heapify(len(self.heap) - 1, self.heap)
            
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
        
        parent = index // 2
        left_child = parent * 2
        right_child = left_child + 1
        
        if(index == 1):
            
            parent = 1
            left_child = 2
            right_child = 3
        
        length = len(array)
        
        minElementOfSubtree = parent
        
        if(index < length and index > 0):
            
            #print "PARENT OF ", str(array[index]), " IS ",  str(array[parent])
            
            if(left_child < len(array)):
                
                if(right_child >= len(array)):
                    
                    minElementOfSubtree = left_child
                    
                else:
            
                    if (array[left_child] <= array[right_child]):
                        
                        minElementOfSubtree = left_child
                        
                        
                    else:
                        minElementOfSubtree = right_child
                    
                if(parent != 0 and array[parent] < array[minElementOfSubtree]):
                    
                    minElementOfSubtree = parent
                    
                
             
            
            if(minElementOfSubtree != parent):
                
               
                self.swap(minElementOfSubtree, parent, array)               
                
                if(parent != 1):
                    self.heapify(parent, array)
                    
                self.heapify((minElementOfSubtree * 2), array)