import unittest
from main import floyd, floyd2

def safe_floyd_warshall(graph):
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

class TestFloyd_Algo(unittest.TestCase):
    def test_iterative(self):
        graph = [[0, 2, 5, float('inf'), float('inf')],
                [float('inf'), 0, 7, 1, 8],
                [float('inf'), float('inf'), 0, 4, float('inf')],
                [float('inf'), float('inf'), float('inf'), 0, 3],
                [float('inf'), float('inf'), 2, float('inf'), 0]]
        expected_result = safe_floyd_warshall (graph)
        self.assertEqual(floyd(graph), expected_result)

    def test_recursive(self):
        graph = [[0, 1, 3, float('inf')], [float('inf'), 0, 1, 2], [float('inf'), float('inf'), 0, 1], [float('inf'), float('inf'), float('inf'), 0]]
        expected_result = safe_floyd_warshall (graph)
        self.assertEqual(floyd2(graph), expected_result)

    def test_recursive2(self):
        graph = [[0, 1, 3, 4], [float('inf'), 0, 1, 2], [float('inf'), float('inf'), 0, 1], [float('inf'), float('inf'), float('inf'), 0]]
        expected_result = safe_floyd_warshall (graph)
        self.assertEqual(floyd2(graph), expected_result)

if __name__ == '__main__':
    unittest.main()
