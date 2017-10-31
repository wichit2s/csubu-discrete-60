
### ประกาศ ฟังก์ชัน 
#def dijkstra(G, s): 
#    Q = { (v,INFINITY,UNDEFINED) for v in G['V'] } 
#    dist[source] = 0                      
#    while len(Q) == 0:
#         u = vertex in Q with min dist[u]  
#         remove u from Q 
#         
#         for each neighbor v of u:           
#             alt ← dist[u] + length(u, v)
#             if alt < dist[v]:               
#                 dist[v] ← alt 
#                 prev[v] ← u 
#
#     return dist[], prev[]
#
# ### ได้เวลาเรียกใช้ ####
G = {
        'V': 'ABCDEF',
        'E': [ 
            ('A','B',3), ('A','E',5), ('A','F',2),
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
print(G)
