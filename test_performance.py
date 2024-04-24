from timeit import default_timer as timer
from functions import floyd, floyd2, safe_floyd_warshall

graph = [[0, 2, 5, float('inf'), float('inf')],
                [float('inf'), 0, 7, 1, 8],
                [float('inf'), float('inf'), 0, 4, float('inf')],
                [float('inf'), float('inf'), float('inf'), 0, 3],
                [float('inf'), float('inf'), 2, float('inf'), 0]]

start = timer()
for i in range(1000):
    safe_floyd_warshall(graph)
end = timer()
print("performance test geeksforgeeks function")
print(end - start)

start = timer()
for i in range(1000):
    floyd(graph)
end = timer()
print("performance test iterative function")
print(end - start)

start = timer()
for i in range(1000):
    floyd2(graph)
end = timer()
print("performance test recursive function")
print(end - start)