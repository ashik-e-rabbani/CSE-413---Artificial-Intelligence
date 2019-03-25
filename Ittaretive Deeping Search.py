# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 03:10:56 2019

@author: Ashik
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 03:03:19 2019

@author: Ashik
"""

vertexList=["0", "1", "2", "3",
            "4", "5", "6"]
edgeList = [(0,1),(0,2),(1,0),
            (1,3),(2,0),(2,4),
            (2,5),(3,1), (4,2),
            (4,6), (5,2),(6,4)]

graphs=(vertexList, edgeList)

def ids(graph, start):
    vertexList, edgeList =graph
  

    visitedList= []
    queue=[start]

    adjacencyList=[]
    for vertex in vertexList:
        adjacencyList.append([])

    

    #fill adjacency list from graph
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    print("Adjacency List After")
    print(adjacencyList)


    #BFS
    while queue:
        current = queue.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.append(neighbor)
               # print("Queue State")
                #print(queue)
        visitedList.append(current)
        
        print("Itaration ",visitedList)
        
        

    



ids(graphs, 0)