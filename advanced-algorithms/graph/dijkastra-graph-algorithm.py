import unittest
import math
import sys


class MinPriorityQueue:

    def __init__(self, max_size):
        self.arr = [None for i in range(max_size+1)]
        self.size = 0

    def get_coll(self):
        return [None if item is None else item.distance for item in self.arr]

    def is_empty(self):
        return self.size == 0

    def insert(self, item):
        self.size += 1
        index = self.size
        self.arr[index] = item
        self._swim(index)

    def del_min(self):
        if self.is_empty():
            return None
        min = self.arr[1]
        self._exchange(1, self.size)
        self.size -= 1
        self.arr[self.size+1] = None
        self._sink(1)
        return min

    def _is_more(self, i, j):
        return self.arr[i].distance > self.arr[j].distance

    def _exchange(self, i, j):
        t = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = t

    def _swim(self, k):
        while k > 1 and self._is_more(k//2, k):
            self._exchange(k//2, k)
            k = k//2

    def _sink(self, k):
        while 2*k <= self.size:
            j = k*2
            if j < self.size and self._is_more(j, j+1):
                j += 1
            if not self._is_more(k, j):
                break
            self._exchange(k, j)
            k = j


class Pair(object):
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance

# Helper Class


class GraphEdge(object):
    def __init__(self, destinationNode, distance):
        self.node = destinationNode
        self.distance = distance

# Helper Classes


class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))

    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    # adds an edge between node1 and node2 in both directions
    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)


def get_distance(node, node_name):
    for edge in node.edges:
        if edge.node.value == node_name:
            return edge.distance
    raise Exception('Node '+node_name + ' not in edges.')


def dijkstra(graph, source, target):
    result = {}
    result[source.value] = 0
    for node in graph.nodes:
        if (node != source):
            result[node.value] = sys.maxsize
    queue = MinPriorityQueue(len(graph.nodes))
    queue.insert(Pair(source, 0))
    while not queue.is_empty():
        pair = queue.del_min()
        if pair.node.value == target.value:
            return result[pair.node.value]
        for edge in pair.node.edges:
            distance_to_neighbour = pair.distance + edge.distance
            if result[edge.node.value] > distance_to_neighbour:
                result[edge.node.value] = distance_to_neighbour
                queue.insert(Pair(edge.node, distance_to_neighbour))

class Tests(unittest.TestCase):

    def test_1(self):
        # Create a graph
        node_u = GraphNode('U')
        node_d = GraphNode('D')
        node_a = GraphNode('A')
        node_c = GraphNode('C')
        node_i = GraphNode('I')
        node_t = GraphNode('T')
        node_y = GraphNode('Y')

        graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])

        # add_edge() function will add an edge between node1 and node2 in both directions
        graph.add_edge(node_u, node_a, 4)
        graph.add_edge(node_u, node_c, 6)
        graph.add_edge(node_u, node_d, 3)
        graph.add_edge(node_d, node_c, 4)
        graph.add_edge(node_a, node_i, 7)
        graph.add_edge(node_c, node_i, 4)
        graph.add_edge(node_c, node_t, 5)
        graph.add_edge(node_i, node_y, 4)
        graph.add_edge(node_t, node_y, 5)

        result = dijkstra(graph, node_u, node_y)
        # Shortest Distance from U to Y is 14
        print('Shortest Distance from {} to {} is {}'.format(
            node_u.value, node_y.value, result))
        self.assertEqual(14, result)

    def test_2(self):
        # Test Case 2
        node_A = GraphNode('A')
        node_B = GraphNode('B')
        node_C = GraphNode('C')

        graph = Graph([node_A, node_B, node_C])

        graph.add_edge(node_A, node_B, 5)
        graph.add_edge(node_B, node_C, 5)
        graph.add_edge(node_A, node_C, 10)

        result = dijkstra(graph, node_A, node_C)
        # Shortest Distance from A to C is 10
        print('Shortest Distance from {} to {} is {}'.format(
            node_A.value, node_C.value, result))
        self.assertEqual(10, result)

    def test_3(self):
        node_A = GraphNode('A')
        node_B = GraphNode('B')
        node_C = GraphNode('C')
        node_D = GraphNode('D')
        node_E = GraphNode('E')

        graph = Graph([node_A, node_B, node_C, node_D, node_E])

        graph.add_edge(node_A, node_B, 3)
        graph.add_edge(node_A, node_D, 2)
        graph.add_edge(node_B, node_D, 4)
        graph.add_edge(node_B, node_E, 6)
        graph.add_edge(node_B, node_C, 1)
        graph.add_edge(node_C, node_E, 2)
        graph.add_edge(node_E, node_D, 1)

        result = dijkstra(graph, node_A, node_C)
        # Shortest Distance from A to C is 4
        print('Shortest Distance from {} to {} is {}'.format(
            node_A.value, node_C.value, result))
        self.assertEqual(4, result)


    def test_4(self):
        """

            A -(1)- B -(2)- C
            |               |
            3               6
            |               |
            E -(4)- D -(5)- F
        """    


        # Create a graph
        node_a = GraphNode('A')
        node_b = GraphNode('B')
        node_c = GraphNode('C')
        node_d = GraphNode('D')
        node_f = GraphNode('F')
        node_e = GraphNode('E')

        graph = Graph([node_a, node_b, node_c, node_d, node_f,node_e])

        # add_edge() function will add an edge between node1 and node2 in both directions
        graph.add_edge(node_a, node_b, 1)
        graph.add_edge(node_b, node_c, 2)
        graph.add_edge(node_a, node_e, 3)
        graph.add_edge(node_e, node_d, 4)
        graph.add_edge(node_d, node_f, 5)
        graph.add_edge(node_c, node_f, 6)

        self.assertEqual(9, dijkstra(graph, node_a, node_f))
        self.assertEqual(0, dijkstra(graph, node_a, node_a))
        self.assertEqual(1, dijkstra(graph, node_a, node_b))
        self.assertEqual(7, dijkstra(graph, node_a, node_d))


if __name__ == '__main__':
    unittest.main()
