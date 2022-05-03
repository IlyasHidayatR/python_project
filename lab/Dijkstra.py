#graf with algoritm Dijkstra
import sys
import math
import time

# graph = {
#     'A': {'B': 2, 'C': 4},
#     'B': {'A': 2, 'C': 3, 'D': 8},
#     'C': {'A': 4, 'B': 3, 'E': 5, 'D': 2},
#     'D': {'B': 8, 'C': 2, 'E': 11, 'F': 22},
#     'E': {'C': 2, 'D': 11, 'F': 1},
#     'F': {'D': 22, 'E': 1}
# }
graph = {}
sum_vertex = int(input('Enter the number of vertex: '))
for i in range (sum_vertex):
    vertex = input('Enter the vertex: ') # input the vertex
    graph[vertex] = {input('Enter the neighbor: '): int(input('Enter the distance: ')) for i in range(int(input('Enter the number of neighbors: ')))} # add the vertex and the neighbors to the graph


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

    for vertex in nodes: # set initial distances to infinity
        if vertex == start: # and previous to None
            distances[vertex] = 0 # except start
        else: # and previous to itself
            distances[vertex] = math.inf # infinity
            previous[vertex] = None # except start

    # while there are still nodes to be processed
    while nodes: # while there are nodes
        min_node = None # minimum node
        for node in nodes: # find the node with the minimum distance
            if min_node is None: # if first iteration
                min_node = node # set the first node
            elif distances[node] < distances[min_node]: # if not first iteration
                min_node = node # set the node with the minimum distance
        if distances[min_node] == math.inf: # if the minimum distance is infinity
            break # there is no way to get to the end
        nodes.remove(min_node) # remove the minimum node from the nodes
        for neighbor, distance in graph[min_node].items(): # for each neighbor of the minimum node
            alt = distances[min_node] + distance # calculate the alternative distance
            if alt < distances[neighbor]: # if the alternative distance is less than the current distance
                distances[neighbor] = alt # set the alternative distance
                previous[neighbor] = min_node # set the previous node

    # build the path
    current_node = end # set the current node to the end node
    while current_node != start: # while the current node is not the start node
        try: # try to get the previous node
            path.insert(0, current_node) # insert the current node into the path
            current_node = previous[current_node] # set the current node to the previous node
        except KeyError: # if there is no previous node
            print('Path not found') # there is no path
            sys.exit() # exit the program
    path.insert(0, start) # insert the start node into the path
    if distances[end] != math.inf: # if the end node has a distance
        print(f'steps: {len(path) - 1}, distance: {distances[end]}') # print the number of stops and the distance
        print(' '.join(path)) # print the path
    else: # if the end node has no distance
        print('Path not found') # there is no path

try:
    start = str(input('Enter the start node: '))
    end = str(input('Enter the end node: '))
    time_start = time.time()
    dijkstra(graph, start, end)
    time_end = time.time()
    print(f'Time: {time_end - time_start}')
except KeyError:
    print('The node does not exist')