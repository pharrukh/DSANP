import unittest

def merge(arr1, arr2):
    i = 0
    j = 0

    l = []
    while True:
        if i == len(arr1):
            if j == len(arr2):
                return l
            l.append(arr2[j])
            j += 1
        elif j == len(arr2):
            if i == len(arr1):
                return l
            l.append(arr1[i])
            i += 1
        elif arr1[i] < arr2[j]:
            l.append(arr1[i])
            i += 1
        else:
            l.append(arr2[j])
            j += 1

def merge_sort(arr):
    # if it is one return
    length = len(arr)
    if length <= 1:
        return arr
    # split the collection while it is more than one
    # if number of elements is odd, leave the first element ??
    # split the collection into two
    mid = length // 2
    left = merge_sort(arr[mid:])
    right = merge_sort(arr[:mid])
    # merge two ordered collections into one

    # return ordered collection
    return merge(left, right)

class MergeSortTests(unittest.TestCase):

    def test_merge_0(self):
        result = merge([1], [])
        self.assertListEqual(result, [1])

    def test_merge_1(self):
        result = merge([], [1])
        self.assertListEqual(result, [1])

    def test_merge_2(self):
        result = merge([1], [1])
        self.assertListEqual(result, [1, 1])

    def test_merge_3(self):
        result = merge([2], [1])
        self.assertListEqual(result, [1, 2])

    def test_merge_4(self):
        result = merge([1], [2])
        self.assertListEqual(result, [1, 2])

    def test_merge_5(self):
        result = merge([1,2,4,5], [3,4,5,6, 7, 8])
        self.assertListEqual(result, [1, 2, 3, 4, 4, 5, 5, 6, 7, 8])

    def test_0(self):
        arr = []
        result = merge_sort(arr)
        self.assertListEqual(result, [])

    def test_1(self):
        arr = [20, 1, 10, 5, 2]
        result = merge_sort(arr)
        self.assertListEqual(result, [1,2,5,10,20])

    def test_2(self):
        arr = [20]
        result = merge_sort(arr)
        self.assertListEqual(result, [20])

    def test_3(self):
        arr = [10,9,8,7,6,5,4,3,2,1]
        result = merge_sort(arr)
        self.assertListEqual(result, [1,2,3,4,5,6,7,8,9,10])

    def test_4(self):
        arr = [1,1,1,1,1,1]
        result = merge_sort(arr)
        self.assertListEqual(result, [1,1,1,1,1,1])

if __name__ == '__main__':
    unittest.main()