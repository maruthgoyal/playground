This program performs breadth first search on a given graph G with vertices V and edges E.

Procedure:

1. Set i to 0
2. Create a dictionary D of processed nodes
2. L is a list of all nodes on level i
3. M is a list of all nodes on level i+1
3. For each node V in L, see all of its neighbors U1, U2...
  4. If Un is not in D, put it in D and set its parent to V, add it to M
5. Set L = M
6. If L is empty, stop
7. Else, go back to step #3
