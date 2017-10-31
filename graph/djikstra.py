### ประกาศ ฟังก์ชัน 
def dijkstra(G, s):

    #create vertex set Q

    #for each vertex v in Graph:             // Initialization
    #    dist[v] ← INFINITY                  // Unknown distance from source to v
    #    prev[v] ← UNDEFINED                 // Previous node in optimal path from source
    #    add v to Q                          // All nodes initially in Q (unvisited nodes)
    Q = { (v,INFINITY,UNDEFINED) for v in G['V'] }

    dist[source] = 0                        // Distance from source to source
     
     while Q is not empty:
         u ← vertex in Q with min dist[u]    // Node with the least distance
                                                     // will be selected first
         remove u from Q 
         
         for each neighbor v of u:           // where v is still in Q.
             alt ← dist[u] + length(u, v)
             if alt < dist[v]:               // A shorter path to v has been found
                 dist[v] ← alt 
                 prev[v] ← u 

     return dist[], prev[]

 ### ได้เวลาเรียกใช้ ####
 G = {
   'V': 'ABCDEF',
   'E': [ 
       ('A','B',3), ('A','E',5), ('A','F',2) 
       ('B','C',3),
       ('C','F',2), ('C','D',4),
       ('D','E',5),
       ('E','F',4)
   ] 
}
G = [ 
    # 'A'  'B'  'C'  'D'  'E'  'F'
    [   0,   3,   0,   0,   5,   2 ], # 'A'
    [   3,   0,   3,   0,   0,   0 ], # 'B'
    [   0,   3,   0,   4,   0,   2 ], # 'C'
    [   0,   0,   4,   0,   5,   0 ], # 'D'
    [   5,   0,   0,   5,   0,   4 ], # 'E'
    [   2,   0,   2,   0,   4,   0 ]  # 'F'
]
