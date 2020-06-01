import unittest

def sort_a_little_bit(items, start_index, end_index):
    left_index = start_index
    partition_index = end_index
    partition = items[partition_index]

    while partition_index != left_index:
        item = items[left_index]

        if item <= partition:
            left_index += 1
            continue
        
        items[left_index] = items[partition_index-1]
        items[partition_index-1] = partition
        items[partition_index] = item

        partition_index -= 1

    return partition_index

def sort_all(items, start_index, end_index):
    if start_index >= end_index:
        return
    
    partition_index = sort_a_little_bit(items, start_index, end_index)
    sort_all(items, start_index, partition_index - 1)
    sort_all(items, partition_index + 1, end_index)

def quicksort(items):
    sort_all(items, 0, len(items)-1)

class Tests(unittest.TestCase):

    def test_0(self):
        items = [8, 3, 1, 7, 0, 10, 2]
        result = [0, 1, 2, 7, 3, 10, 8]
        pivot_index = sort_a_little_bit(items, 0, len(items) - 1)
        self.assertListEqual(items, result)
        self.assertEqual(pivot_index, 2)

    def test_sort_0(self):
        items = [8, 3, 1, 7, 0, 10, 2]
        result = [0, 1, 2, 3, 7, 8, 10]
        quicksort(items)
        self.assertListEqual(items, result)

    def test_sort_1(self):
        items = [2,2,2,2,3,3,1,1,1,0,20,30,50]
        result = [0,1,1,1,2,2,2,2,3,3,20,30,50]
        quicksort(items)
        self.assertListEqual(items, result)

if __name__ == '__main__':
    unittest.main()