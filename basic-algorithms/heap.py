import unittest

class Heap:
    def __init__(self, initial_size):
        self.max_size = initial_size
        self.cbt = [None for _ in range(initial_size)]        # initialize arrays
        self.next_index = 0                                   # denotes next index where new element should go
    
    def _is_less(self, child_index, parent_index):
        return self.cbt[child_index] > self.cbt[parent_index] 

    def _swap(self, i, j):
        temp = self.cbt[j]
        self.cbt[j] = self.cbt[i]
        self.cbt[i] = temp

    def _up_heapify(self, child_index):
        while True:
            if child_index == 0:
                break
            parent_index = (child_index - 1)//2
            if self._is_less(child_index, parent_index):
                break
            self._swap(child_index, parent_index)
            child_index = parent_index

    def _next_min_child_index(self, i):
        last_item_index = self.next_index - 1
        next_left = 2*i+1
        next_right = 2*i+2
        if next_left > last_item_index and next_right > last_item_index:
            return None

        if next_left <= last_item_index and next_right > last_item_index:
            return next_left
        
        if self.cbt[next_left] < self.cbt[next_right]:
            return next_left

        return next_right


    def _down_heapify(self):
        cur_index = 0
        last_item_index = self.next_index - 1
        while True:
            if cur_index > last_item_index:
                break
            next_min_index = self._next_min_child_index(cur_index)
            if not next_min_index:
                break
            if next_min_index > last_item_index:
                break
            self._swap(cur_index, next_min_index)
            cur_index = next_min_index

    def insert(self, data):
        """
        Insert `data` into the heap
        """
        self.cbt[self.next_index] = data
        if self.next_index != 0:
            self._up_heapify(self.next_index)
        self.next_index += 1

        if self.next_index > self.max_size:
            new_arr = []
            for i in range(len(self.cbt)*2):
                if i < len(self.cbt):
                    new_arr[i] = self.cbt[i]
                new_arr[i] = None
            self.cbt = new_arr 


    def remove(self):
        root = self.cbt[0]
        self._swap(0, self.next_index - 1)
        self.cbt[self.next_index - 1] = None
        self._down_heapify()
        self.next_index -= 1
        return root



        


class HeapTest(unittest.TestCase):

    def test_1(self):
        heap = Heap(5)
        heap.insert(1)
        self.assertEqual(heap.next_index, 1)
        self.assertListEqual(heap.cbt, [1, None, None, None, None])

    def test_2(self):
        heap = Heap(5)
        heap.insert(1)
        self.assertEqual(heap.next_index, 1)
        heap.insert(2)
        self.assertEqual(heap.next_index, 2)
        heap.insert(3)
        self.assertEqual(heap.next_index, 3)
        self.assertListEqual(heap.cbt, [1, 2, 3, None, None])

    def test_3(self):
        heap = Heap(10)
        heap.insert(10)
        heap.insert(9)
        self.assertListEqual(heap.cbt, [9, 10, None, None, None, None, None, None, None, None])
        heap.insert(8)
        self.assertListEqual(heap.cbt, [8, 10, 9, None, None, None, None, None, None, None ])
        heap.insert(7)
        self.assertListEqual(heap.cbt, [7, 8, 9, 10, None, None, None, None, None, None ])
        heap.insert(6)
        heap.insert(5)
        heap.insert(4)
        heap.insert(3)
        heap.insert(2)
        heap.insert(1)
        self.assertListEqual(heap.cbt, [1, 2, 5, 4, 3, 9, 6, 10, 7, 8])

    def test_4(self):
        heap = Heap(10)
        heap.insert(10)
        heap.insert(9)
        heap.insert(8)
        heap.insert(7)
        heap.insert(6)
        heap.insert(5)
        heap.insert(4)
        heap.insert(3)
        heap.insert(2)
        heap.insert(1)
        self.assertListEqual(heap.cbt, [1, 2, 5, 4, 3, 9, 6, 10, 7, 8])
        for i in range(1, 11):
            print(i)
            self.assertEqual(heap.remove(), i)

if __name__ == '__main__':
    unittest.main()