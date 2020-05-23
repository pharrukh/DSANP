import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class MinPriorityQueue:

    def __init__(self, max_size):
        self.arr = [None for i in range(max_size+1)]
        self.size = 0

    def get_coll(self):
        return [None if node is None else node.value for node in self.arr]
    
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
        return self.arr[i].value > self.arr[j].value

    def _exchange(self, i, j):
        t = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = t

    def _swim(self, k):
        while k>1 and self._is_more(k//2, k):
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


class MinPriorityQueueTests(unittest.TestCase):

    def test(self):
        mpq = MinPriorityQueue(5)
        mpq.insert(Node(1))
        self.assertEqual(mpq.get_coll(), [None, 1, None, None, None, None])
        mpq.insert(Node(2))
        self.assertEqual(mpq.get_coll(), [None, 1, 2, None, None, None])
        mpq.insert(Node(3))
        self.assertEqual(mpq.get_coll(), [None, 1, 2, 3, None, None])
        mpq.insert(Node(2))
        self.assertEqual(mpq.get_coll(), [None, 1, 2, 3, 2, None])
        mpq.insert(Node(1))
        self.assertEqual(mpq.get_coll(), [None, 1, 1, 3, 2, 2])
        min = mpq.del_min()
        self.assertEqual(min.value, 1)
        self.assertEqual(mpq.get_coll(), [None, 1, 2, 3, 2, None])
        min = mpq.del_min()
        self.assertEqual(min.value, 1)
        self.assertEqual(mpq.get_coll(), [None, 2, 2, 3, None, None])
        min = mpq.del_min()
        self.assertEqual(min.value, 2)
        self.assertEqual(mpq.get_coll(), [None, 2, 3, None, None, None])
        min = mpq.del_min()
        self.assertEqual(min.value, 2)
        self.assertEqual(mpq.get_coll(), [None, 3, None, None, None, None])
        min = mpq.del_min()
        self.assertEqual(min.value, 3)
        self.assertEqual(mpq.get_coll(), [None, None, None, None, None, None])
        min = mpq.del_min()
        self.assertEqual(min, None)
        self.assertEqual(mpq.get_coll(), [None, None, None, None, None, None])
        
if __name__ == '__main__':
    unittest.main()