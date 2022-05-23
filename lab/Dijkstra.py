#graf with algoritm Dijkstra
import sys
import math
import time

graph = {
    'A': {'B': 2, 'C': 18, 'D': 8},
    'B': {'A': 2, 'E': 4},
    'C': {'A': 18, 'E': 10, 'F': 12},
    'D': {'A': 8, 'F': 5, 'G': 13},
    'E': {'B': 4, 'C': 10, 'H': 11},
    'F': {'C': 12, 'D': 5, 'H': 7, 'J': 6},
    'G': {'D': 13, 'J': 14},
    'H': {'E': 11, 'F': 7, 'I': 9},
    'I': {'H': 9, 'J': 17},
    'J': {'F': 6, 'G': 14, 'I': 17}
}
graph_1 = {
    'A': {'B': 6, 'C': 4, 'D': 7},
    'B': {'A': 6, 'E': 9},
    'C': {'A': 4, 'E': 12, 'F': 8},
    'D': {'A': 7, 'F':11, 'G': 14},
    'E': {'B': 9, 'C': 12, 'H': 16},
    'F': {'C': 8, 'D': 11, 'H': 3, 'J': 17},
    'G': {'D': 14, 'J': 5},
    'H': {'E': 16, 'F': 3, 'I': 2},
    'I': {'H': 2, 'J': 13},
    'J': {'F': 17, 'G': 5, 'I': 13}
}
# graph = {}
# sum_vertex = int(input('Enter the number of vertex: '))
# for i in range (sum_vertex):
#     vertex = input('Enter the vertex: ') # input the vertex
#     graph[vertex] = {input('Enter the neighbor: '): int(input('Enter the distance: ')) for i in range(int(input('Enter the number of neighbors: ')))} # add the vertex and the neighbors to the graph


def dijkstra(graph, start, end):
    """
    :param graph: dict
    :param start: str
    :param end: str
    :return: list
    """
    distances = {} # dictionary of final distances
    previous = {} # dictionary of previous nodes
    path = [] # list of nodes in a path
    nodes = set(graph.keys()) # set of all nodes in a graph

    for vertex in nodes: # set initial distances to infinity and previous (complexity O(n))
        if vertex == start: # and previous to None for the start node (complexity O(1))
            distances[vertex] = 0 # except start
        else: # and previous to itself (complexity O(1))
            distances[vertex] = math.inf # infinity
            previous[vertex] = None # except start
    #compleksity: O(n)

    # while there are still nodes to be processed
    while nodes: # while there are nodes (O(n))
        min_node = None # minimum node
        for node in nodes: # find the node with the minimum distance (O(n))
            if min_node is None: # if first iteration (O(1))
                min_node = node # set the first node
            elif distances[node] < distances[min_node]: # if not first iteration (O(n))
                min_node = node # set the node with the minimum distance
        if distances[min_node] == math.inf: # if the minimum distance is infinity (O(1))
            break # there is no way to get to the end
        nodes.remove(min_node) # remove the minimum node from the nodes
        for neighbor, distance in graph[min_node].items(): # for each neighbor of the minimum node (O(n))
            alt = distances[min_node] + distance # calculate the alternative distance (O(1))
            if alt < distances[neighbor]: # if the alternative distance is less than the current distance (O(1))
                distances[neighbor] = alt # set the alternative distance as the current distance (O(1))
                previous[neighbor] = min_node # set the previous node as the minimum node (O(1))
    #compleksity: O(n) + O(n^2) + O(n) = O(n^2)


    # build the path
    current_node = end # set the current node to the end node
    while current_node != start: # while the current node is not the start node (O(n))
        try: # try to get the previous node
            path.insert(0, current_node) # insert the current node into the path (O(1))
            current_node = previous[current_node] # set the current node to the previous node
        except KeyError: # if there is no previous node
            print('Path not found') # there is no path to the end node from the start node (O(1))
            sys.exit() # exit the program
    path.insert(0, start) # insert the start node into the path
    if distances[end] != math.inf: # if the end node has a distance (O(1))
        print(f'steps: {len(path) - 1}, distance: {distances[end]}') # print the number of stops and the distance (O(1))
        print(' '.join(path)) # print the path
    else: # if the end node has no distance
        print('Path not found') # there is no path
    #compleksity: O(n) + O(1) + O(1) + O(1) + O(1) = O(n)

try:
    print('Graph Pertama:')
    start = str(input('Enter the start node: '))
    end = str(input('Enter the end node: '))
    time_start = time.time()
    dijkstra(graph, start, end) #compleksity: O(n) + O(n^2) + O(n) = O(n^2)
    time_end = time.time()
    print(f'Time: {time_end - time_start}')
    print('\n')
    print('Graph Kedua:')
    start_1 = str(input('Enter the start node: '))
    end_1 = str(input('Enter the end node: '))
    time_start_1 = time.time()
    dijkstra(graph_1, start_1, end_1) #compleksity: O(n) + O(n^2) + O(n) = O(n^2)
    time_end_1 = time.time()
    print(f'Time: {time_end_1 - time_start_1}')
except KeyError:
    print('The node does not exist')