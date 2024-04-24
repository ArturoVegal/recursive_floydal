import itertools

def floyd(distance):
    """
    A simple implementation of Floyd's algorithm
    """
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

# Example usage:
# Initialize the graph distance matrix
MAX_LENGTH = 5  # Example value, replace with your actual value
graph = [[0, 2, 5, float('inf'), float('inf')],
         [float('inf'), 0, 7, 1, 8],
         [float('inf'), float('inf'), 0, 4, float('inf')],
         [float('inf'), float('inf'), float('inf'), 0, 3],
         [float('inf'), float('inf'), 2, float('inf'), 0]]

# Call the function with the graph matrix
floyd(graph)


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

# Example usage:
graph = [[0, 2, 5, float('inf'), float('inf')],
         [float('inf'), 0, 7, 1, 8],
         [float('inf'), float('inf'), 0, 4, float('inf')],
         [float('inf'), float('inf'), float('inf'), 0, 3],
         [float('inf'), float('inf'), 2, float('inf'), 0]]

# print (floyd2(graph))
