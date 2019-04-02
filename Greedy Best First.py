Heuristic_value_graph = {\
            'Natore': {'Sirajgonj': 248, 'Naogon': 369, 'Kushtia': 324},\
            'Naogon': {'Natore': 361, 'Bogra': 375},\
            'Bogra': {'Naogon': 369, 'Sirajgonj': 248},\
            'Sirajgonj': {'Natore': 361, 'Bogra': 375, 'Mymenshing': 171, 'Tangail': 188},\
            'Kushtia': {'Natore': 361, 'Rajbari': 239},\
            'Rajbari': {'Kushtia': 324, 'Magura': 236},\
            'Magura': {'Rajbari': 239, 'Faridpur': 237},\
            'Faridpur': {'Magura': 236, 'Manikgonj': 155},\
            'Manikgonj': {'Faridpur': 237, 'Tangail': 188, 'Gazipur': 95},\
            'Tangail': {'Sirajgonj': 248, 'Manikgonj': 155, 'Gazipur': 95},\
            'Mymenshing': {'Sirajgonj': 248, 'Dhaka': 0},\
            'Gazipur': {'Tangail': 188, 'Manikgonj': 155, 'Dhaka': 0},\
            'Dhaka': {'Mymenshing': 171, 'Gazipur': 95, 'Narayangonj': 85, 'Narshindi': 105},\
            'Narayangonj': {'Dhaka': 0},\
            'Narshindi': {'Dhaka': 0, 'Kishorgonj': 155},\
            'Kishorgonj': {'Netrokona': 204, 'Narshindi': 105},\
            'Netrokona': {'Kishorgonj': 155, 'Sunamgonj': 245},\
            'Sunamgonj': {'Netrokona': 204}\
        }
        
        
        
        
        
GRAPH_with_path_cost = {\
            'Natore': {'Sirajgonj': 135, 'Naogon': 70, 'Kushtia': 113},\
            'Naogon': {'Natore': 70, 'Bogra': 66},\
            'Bogra': {'Naogon': 66, 'Sirajgonj': 146},\
            'Sirajgonj': {'Natore': 135, 'Bogra': 146, 'Mymenshing': 94, 'Tangail': 75},\
            'Kushtia': {'Natore': 113, 'Rajbari': 106},\
            'Rajbari': {'Kushtia': 106, 'Magura': 65},\
            'Magura': {'Rajbari': 65, 'Faridpur': 70},\
            'Faridpur': {'Magura': 70, 'Manikgonj': 115},\
            'Manikgonj': {'Faridpur': 115, 'Tangail': 141, 'Gazipur': 133},\
            'Tangail': {'Sirajgonj': 75, 'Manikgonj': 141, 'Gazipur': 92},\
            'Mymenshing': {'Sirajgonj': 94, 'Dhaka': 206},\
            'Gazipur': {'Tangail': 92, 'Manikgonj': 133, 'Dhaka': 96},\
            'Dhaka': {'Mymenshing': 206, 'Gazipur': 96, 'Narayangonj': 90, 'Narshindi': 80},\
            'Narayangonj': {'Dhaka': 90},\
            'Narshindi': {'Dhaka': 80, 'Kishorgonj': 110},\
            'Kishorgonj': {'Netrokona': 210, 'Narshindi': 110},\
            'Netrokona': {'Kishorgonj': 210, 'Sunamgonj': 145},\
            'Sunamgonj': {'Netrokona': 145}\
        }       
        
        
        
        
        
def dfs_paths(source, destination, path=None):

    if path is None:
        path = [source]
    if source == destination:
        yield path
    for next_node in set(Heuristic_value_graph[source].keys()) - set(path):
        yield from dfs_paths(next_node, destination, path + [next_node])
        
def ucs(source, destination):
    
    from queue import PriorityQueue
    priority_queue, visited = PriorityQueue(), {}
    priority_queue.put((0, source, [source]))
    visited[source] = 0
    while not priority_queue.empty():
        (cost, vertex, path) = priority_queue.get()
        if vertex == destination:
            return cost, path
        for next_node in Heuristic_value_graph[vertex].keys():
            current_cost = cost + Heuristic_value_graph[vertex][next_node]
            
            if not next_node in visited or visited[next_node] >= current_cost:
                visited[next_node] = current_cost
                priority_queue.put((current_cost, next_node, path + [next_node]))
        print('->',cost)

def main():
    """Main function"""
    print("\nGreedy Best First Search\n----------------------\n")
    
    print('(Your now at) :', end=' ')
    source = input().strip()
    print('(Where to go) :', end=' ')
    goal = input().strip()
    if source not in Heuristic_value_graph or goal not in Heuristic_value_graph:
        print('ERROR: CITY DOES NOT EXIST.')
    else:
        print('\nAll path to Destination \n----------------------------')
        paths = dfs_paths(source, goal)
        for path in paths:
            print(' -> '.join(city for city in path))
        print('\nChoosen Cumulative Heurestic Value :')
        cost, cheapest_path = ucs(source, goal)
        
        print('\nShortest Path : \n-----------------')
        print(' -> '.join(city for city in cheapest_path))
        print('\nFinal Cost from Heurestic Traversal =', cost)
        
        print('\nFinal Cost of visiting : ',end='->')
        fl = []
             
        total_path_cost = 0      
        fl.append(cheapest_path)
       
        for i in range(0,len(fl[0])-1):
            
            if (i<= len(fl[0])):
                this_node =fl[0][i]
                next_node =fl[0][i+1]
            
                get_the_path_value = GRAPH_with_path_cost.get(this_node).get(next_node)
                print(get_the_path_value,end='->->->')
            
                total_path_cost= get_the_path_value+total_path_cost
                 
        print('\nTotal : ',total_path_cost)
        
        

if __name__ == '__main__':
    main()
