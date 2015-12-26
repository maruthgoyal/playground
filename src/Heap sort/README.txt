Implements the heap sort algorithm for sorting an array A of size N in O(N log_2 N) time.

Procedure:
0. Create a min-heap
1. Add all elements of A to the min-heap
2. Create a new list L
3. While the min-heap is not empty,
      perform extract-min and add that element to L
4. return L

min-heap:
1. Nearly complete binary tree
2. Every parent node is <= its children
