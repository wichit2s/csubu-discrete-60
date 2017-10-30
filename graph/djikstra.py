### ประกาศ ฟังก์ชัน 
def dijkstra(G, s):

    #create vertex set Q

    #for each vertex v in Graph:             // Initialization
    #    dist[v] ← INFINITY                  // Unknown distance from source to v
    #    prev[v] ← UNDEFINED                 // Previous node in optimal path from source
    #    add v to Q                          // All nodes initially in Q (unvisited nodes)
    Q = { (v,INFINITY,UNDEFINED) for v in G['V'] }

    dist[source] ← 0                        // Distance from source to source
     
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
   'E': [], 
}
