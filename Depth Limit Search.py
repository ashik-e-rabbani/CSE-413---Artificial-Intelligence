# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 20:16:58 2019

@author: Ashik
"""

graph1 = {
    '0' : ['1','2'],
    '1' : ['0','3'],
    '2' : ['0','4','5'],
    '3' : ['1'],
    '4' : ['2','6'],
    '5' : ['2'],
    '6' : ['4']

    
}

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
    return visited

visited = dfs(graph1,'0', [])

# time to limit it

level = [
          ['0'],             #level 0
          ['1','2'],         #level 1
          ['3','4','5'],     #level 2
          ['6'],
          []                #one level is extended for amar wish
          
          ]


print(" \n Depth Limit Search")
print(" ------------------ \n")
 
search_limit = int(input("Enter level: "))
level_size = len(level)


for i in range (search_limit+1,level_size):
    for j in range (0,len(level[i])):
        visited.remove(level[i][j])


print(visited)
