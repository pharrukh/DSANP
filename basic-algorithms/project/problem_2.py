import unittest

def recursive_binary_search(arr, number, start, end):
    if end-start+1 <= 0:
        return -1
    else:
        middle = start + (end - start) // 2
        if arr[middle] == number:
            return middle
        else:
            if number < arr[middle]:
                return recursive_binary_search(arr, number, start, middle-1)
            else:
                return recursive_binary_search(arr, number, middle+1, end)


def get_middle_el(arr, start, end):
    middle = start + (end - start) // 2
    return (middle, arr[middle])


def find_pivot(arr, start, end):

    if end < start:
        return -1
    if end == start:
        return start

    mid = (start + end)//2

    if mid < end and arr[mid] > arr[mid + 1]:
        return mid
    if mid > start and arr[mid] < arr[mid - 1]:
        return (mid-1)
    if arr[start] >= arr[mid]:
        return find_pivot(arr, start, mid-1)
    else:
        return find_pivot(arr, mid + 1, end)


def rotated_array_search(arr, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start = 0
    end = len(arr) - 1
    middle, el = get_middle_el(arr, start, end)

    if number == el:
        return middle

    pivot = find_pivot(arr, start, end)

    if pivot == -1:
        return -1

    left_result = recursive_binary_search(arr, number, 0, pivot)
    right_result = recursive_binary_search(arr, number, pivot+1, len(arr)-1)

    if left_result != -1:
        return left_result
    elif right_result != -1:
        return right_result
    return -1


def linear_search(arr, number):
    for index, element in enumerate(arr):
        if element == number:
            return index
    return -1


class Tests(unittest.TestCase):

    def test_0(self):
        coll = [6, 7, 8, 9, 10, 1, 2, 3, 4]
        n = 6
        linear_search_result = linear_search(coll, n)
        rotated_array_search_result = rotated_array_search(coll, n)
        self.assertEqual(rotated_array_search_result, linear_search_result)

    def test_1(self):
        coll = [6, 7, 8, 9, 10, 1, 2, 3, 4]
        n = 1
        linear_search_result = linear_search(coll, n)
        rotated_array_search_result = rotated_array_search(coll, n)
        self.assertEqual(rotated_array_search_result, linear_search_result)

    def test_2(self):
        coll = [6, 7, 8, 1, 2, 3, 4]
        n = 8
        linear_search_result = linear_search(coll, n)
        rotated_array_search_result = rotated_array_search(coll, n)
        self.assertEqual(rotated_array_search_result, linear_search_result)

    def test_3(self):
        coll = [6, 7, 8, 1, 2, 3, 4]
        n = 1
        linear_search_result = linear_search(coll, n)
        rotated_array_search_result = rotated_array_search(coll, n)
        self.assertEqual(rotated_array_search_result, linear_search_result)

    def test_4(self):
        coll = [6, 7, 8, 1, 2, 3, 4]
        n = 10
        linear_search_result = linear_search(coll, n)
        rotated_array_search_result = rotated_array_search(coll, n)
        self.assertEqual(rotated_array_search_result, linear_search_result)

    def test_5(self):
        coll = [2, 0, 1]
        n = 0
        linear_search_result = linear_search(coll, n)
        rotated_array_search_result = rotated_array_search(coll, n)
        self.assertEqual(rotated_array_search_result, linear_search_result)

    def test_6(self):
        coll = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]
        n = 93
        linear_search_result = linear_search(coll, n)
        rotated_array_search_result = rotated_array_search(coll, n)
        self.assertEqual(rotated_array_search_result, linear_search_result)

    def test_7(self):
        coll = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]
        n = 89
        linear_search_result = linear_search(coll, n)
        rotated_array_search_result = rotated_array_search(coll, n)
        self.assertEqual(rotated_array_search_result, linear_search_result)

    def test_8(self):
        coll = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]
        n = 0
        linear_search_result = linear_search(coll, n)
        rotated_array_search_result = rotated_array_search(coll, n)
        self.assertEqual(rotated_array_search_result, linear_search_result)

    def test_9(self):
        coll = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]
        n = 99
        linear_search_result = linear_search(coll, n)
        rotated_array_search_result = rotated_array_search(coll, n)
        self.assertEqual(rotated_array_search_result, linear_search_result)

    def test_10(self):
        coll = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]
        n = 88
        linear_search_result = linear_search(coll, n)
        rotated_array_search_result = rotated_array_search(coll, n)
        self.assertEqual(rotated_array_search_result, linear_search_result)

    def test_11(self):
        coll = [99, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]
        n = 99
        linear_search_result = linear_search(coll, n)
        rotated_array_search_result = rotated_array_search(coll, n)
        self.assertEqual(rotated_array_search_result, linear_search_result)


if __name__ == '__main__':
    unittest.main()
