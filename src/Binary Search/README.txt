This program searches for a value 'k' in an array A of size N in O(log_2 N) time.

Procedure:

1. Sort A in ascending order  // Can do in descending order too. Will have to make some modifications though
2. Check if the middle element is k
3. If it is 'k', return that index
4. If it is greater than 'k', repeat the procedure on the remaining array on the left of the middle element
5. If it is less than 'k', repeat the procedure on the remaining array on the right of the middle element
6. Go back to step #2
7. Return -1 if element is not in A
