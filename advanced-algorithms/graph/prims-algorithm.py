import unittest
from heapq import heappop, heappush

def map(bridge_config):
    graph = []
    max_island = 0
    for [left_island, right_island, _] in bridge_config:
        if left_island > max_island:
            max_island = left_island
        if right_island > max_island:
            max_island = right_island
    for _ in range(max_island+1):
        graph.append([])
    for [left_island, right_island, distance] in bridge_config:
        graph[left_island].append((right_island, distance))
        graph[right_island].append((left_island, distance))
    return graph


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    if len(bridge_config) == 0:
        raise Exception('Must contain at least one element.')

    graph = map(bridge_config)
    visited = [False for _ in graph]
    total_cost = 0
    min_heap = []
    start_index = 1

    heappush(min_heap, (0, start_index))

    while min_heap:
        distance, island = heappop(min_heap)
        if visited[island]:
            continue
        total_cost += distance
        visited[island] = True
        for new_island, new_distance in graph[island]:
            heappush(min_heap, (new_distance, new_island))
    
    return total_cost



class Tests(unittest.TestCase):

    def test_map_1(self):
        bridge_config = [[1, 2, 1], [2, 3, 4],
                         [1, 4, 3], [4, 3, 2], [1, 3, 10]]
        graph = [[], [(2, 1), (4, 3), (3, 10)], [(1, 1), (3, 4)], [
            (2, 4), (4, 2), (1, 10)], [(1, 3), (3, 2)]]
        result = map(bridge_config)
        for i, vertex in enumerate(result):
            expected_vertex = graph[i]
            self.assertEqual(len(vertex), len(expected_vertex))
            for bridge in vertex:
                self.assertTrue(bridge in expected_vertex)

    def test_1(self):
        num_islands = 4
        bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
        solution = 6

        result = get_minimum_cost_of_connecting(num_islands, bridge_config)
        self.assertEqual(result, solution)

    def test_2(self):
        num_islands = 5
        bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
        solution = 13

        result = get_minimum_cost_of_connecting(num_islands, bridge_config)
        self.assertEqual(result, solution)

    def test_3(self):
        num_islands = 5
        bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
        solution = 31

        result = get_minimum_cost_of_connecting(num_islands, bridge_config)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
