Implements the single source shortest path algorithm by Dijkstra.

Procedure:
1. Create a Priority Queue of all nodes based on their distance from the source vertex
2. Extract the minimum from the queue and set it to V, remove V from the Queue
3. For every neighbor N of V, relax the edge V -> N
4. If queue is empty, stop. Else, go back to 2

Relax:
1. If length of path is shorter than current distance from source vertex, set parent pointer to be V.
