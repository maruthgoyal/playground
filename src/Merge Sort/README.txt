Implements the merge sort algorithm for sorting an array A of size N in O(N log_2 N) time.

Procedure:
1. Split the array into 2 halves recursively till they are of length 1.
2. Merge the 2 arrays.

Merge:
1. Set one array to be the left, the other the right
2. Add smaller of the current element of left and right to the array
