### Graph 2022.11.01
1. Graph data structure:
    |        | space    | traversal | recommended | restriction |
    | -      |   -      |  -        | -           | - |
    | Matrix | O(v^2)   | O(v^2)    |             |   |
    | Dict   | O(v^2\*H)| O(v)      | v           | nested dict, aka out-D, compute parents_dict in advance for some situations |
    | Node   | O(v+e)   | O(v+e)    |             | complex and rarely seen in disconnected graph |
    + data structure transformation can use dict as media e.g. clone graph (node->dict->node)

2. General graph traversal:
    + **Graph** (general) vs **Binary tree** (connected+directed+acyclic): **acyclic doesn't need to record "visit"**
    + Connection:
        + **Connected** (One entry point can go to everywhere) -> visit e.g. Maze, Word search
        + **Disconnected** (Every entry points are needed) -> unvisit e.g. Number of provinces
    + **DFS** is easier and enough:
        + (Recommended) bottom-up recursion 1 or 2 arguments: node, visit/unvisit 
        + stack iteration arguments: while stack, node, visit/unvisit
        + [Note] Revoke traversal need to pop the node after traversal if use recursive-bu-2 so recursive-bu-1 is better e.g. Word Search
    + Traversal not consider unweighted/weighted

3. Topological sort (directed):
    + **Kahn's algorithm (Iteration)**: Remove in-degree=0 nodes gradually (In-D is needed).
    + Applications: Scheduling, Cycle determination e.g. Course scheduling
    
4. Shortest path problem (directed/undirected):
    |            | Dijkstra | Bellman-Ford           |
    | -          | -        | -                      |
    | situation  | positive edge and no step restriction | can have either left |
    | concept    | Initialize distance dict -> get unvisited min dist node (v times)<br>-> triangular update (neighbor times) | Initialize distance dict -> copy distance dict (v times)<br>-> triangular update (all edges times) |
    | time       | Naive:O(v^2)<br>Heap:O(elog(v)) | O(ve) |
    | example    | Network delay time | Cheapest flights within k steps |
    + Dijkstra in naive is recommended since its easier and efficient in general case (dense graph)
    
5. Minimum spanning tree (directed): Prim's algorithm
    + Random pick start -> Initialize edge set -> pick min edge (l,r) then add to tree, add r neighbors edges, remove (x,r) from set (v-1 times)
    + Naive: O(v^2); Heap: O(elog(v))

### Graph 2023.09.18
1. DFS - recursion - O(E+V)
2. BFS - queue - O(E+V) e.g. shortest path problem with equal weights or depth constraint e.g. 127. Word Ladder or 542. 01 matrix
3. Shortest path
    + Dijkstra - heap + distanceToStart - O( (V+E)logV ). Single source non-negative edge
    + Bellman-Ford - Single source - O(VE)
    + Floyd-Warshall - Multiple sources - O(v^3)
4. Minimum spanning tree
    + Prim - heap + distance to MST - O( (E+V)logV ) very similar to Dijkstra
    + Kruskal - Sort edges + Disjoint Set - O(ElogE) has same complexity with Prim
5. Topological sort
    + Kahn - Graph + inDegL - O(V+E)

+ More <=P
    + Eulerian Path
+ More >NP
    + Hamiltonian Path (equal weight)
    + TSP (non-equal weight)
    + Schedueling optimization

### Others
    + subarray: caterpillar
    + subsequence: DP
