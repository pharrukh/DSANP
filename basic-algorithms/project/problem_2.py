import unittest


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
   pass

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
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
        coll = [2 0 1]
        n = 0
        linear_search_result = linear_search(coll, n)
        rotated_array_search_result = rotated_array_search(coll, n)
        self.assertEqual(rotated_array_search_result, linear_search_result)

if __name__ == '__main__':
    unittest.main()