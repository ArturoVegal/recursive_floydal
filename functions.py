import itertools

def safe_floyd_warshall(graph):
    """
    This function is an iterative solution from geeksforgeeks
    """
    # Number of vertices
    n = len(graph)
    
    # Initialize the distance matrix with the given graph
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                 dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
    return dist

def floyd(distance):
    """
    A simple iterative implementation of Floyd's algorithm
    """
    MAX_LENGTH = len(distance)
    for intermediate, start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
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

def floydal_recursive(distance, intermediate, start_node, end_node, MAX_LENGTH):
    # Base case: If start_node and end_node are the same, set distance to 0
    if start_node == end_node:
        distance[start_node][end_node] = 0
        return

    # Base case: if intermediate is beyond the last index, return
    if intermediate >= MAX_LENGTH:
        return

    # Recursive case: update the distance matrix
    current_distance = distance[start_node][end_node]
    new_distance = distance[start_node][intermediate] + distance[intermediate][end_node]
    if new_distance < current_distance:
        distance[start_node][end_node] = new_distance
        # Recur for the next nodes to propagate the possible change
        floydal_recursive(distance, 0, start_node, end_node, MAX_LENGTH)

    # Move to the next intermediate node
    floydal_recursive(distance, intermediate + 1, start_node, end_node, MAX_LENGTH)

def floyd2(distance):
    """
    A wrapper function to call the recursive implementation
    """
    MAX_LENGTH = len(distance)
    for start_node in range(MAX_LENGTH):
        for end_node in range(MAX_LENGTH):
            floydal_recursive(distance, 0, start_node, end_node, MAX_LENGTH)
    # Print the final distance matrix
    return distance
