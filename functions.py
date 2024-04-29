import itertools

from copy import deepcopy

def safe_floyd_warshall(graph):
    """
    This function is an iterative solution from geeksforgeeks
    """
    # Number of vertices
    n = len(graph)

    # Initialize the distance matrix with the given graph
    dist = deepcopy(graph) # Creates a copy
 
    # Floyd-Warshall algorithm
    for k in range(n):   #outer loop
        for i in range(n): #middle loop
            for j in range(n): #inner loop
                 dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j]) #minimun distance is found
    return dist

def floyd(distance):
    """
    A simple iterative implementation of Floyd's algorithm
    """
    max_length = len(distance)
    for intermediate, start_node, end_node in itertools.product(range(max_length), range(max_length), range(max_length)):
        # Assume that if start_node and end_node are the same then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        # Calculate the minimum distance between start_node and end_node
        distance[start_node][end_node] = min(distance[start_node][end_node],
                                              distance[start_node][intermediate] + distance[intermediate][end_node])
    # Print the final distance matrix
    # print(distance)
    return distance

# Recursive Floyd's algorithm exercise

def floydal_recursive(distance, intermediate, start_node, end_node, max_length):
    # Base case: If start_node and end_node are the same, set distance to 0
    if start_node == end_node:
        distance[start_node][end_node] = 0
        return #que hace este return?? hace que termine la funcion 

    # Base case: if intermediate is beyond the last index, return
    if intermediate >= max_length:
        return 

    # Recursive case: update the distance matrix
    current_distance = distance[start_node][end_node]
    new_distance = distance[start_node][intermediate] + distance[intermediate][end_node]
    if new_distance < current_distance:
        distance[start_node][end_node] = new_distance

    # Move to the next intermediate node
    floydal_recursive(distance, intermediate + 1, start_node, end_node, max_length)

def floyd2(distance):
    """
    A wrapper function to call the recursive implementation
    """
    max_length = len(distance)
    for start_node in range(max_length):
        for end_node in range(max_length):
            floydal_recursive(distance, 0, start_node, end_node, max_length)
    # Print the final distance matrix
    return distance
