import unittest

def pair_sum(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    TODO: complete this method to find two numbers such that their sum is equal to the target
    Return the two numbers in the form of a sorted list
    """
    arr.sort()

    left_index = 0
    right_index = len(arr) - 1
    while left_index != right_index:
        if arr[left_index] + arr[right_index] == target:
            return [arr[left_index], arr[right_index]]
        elif arr[left_index] + arr[right_index] > target:
            right_index -= 1
        else:
            left_index += 1
    return [None, None]

class Tests(unittest.TestCase):

    def test_0(self):
        input_list = [2, 7, 11, 15]
        target = 9
        solution = [2, 7]
        self.assertListEqual(pair_sum(input_list, target), solution)

    def test_1(self):
        input_list = [0, 8, 5, 7, 9]
        target = 9
        solution = [0, 9]
        self.assertListEqual(pair_sum(input_list, target), solution)

    def test_2(self):
        input_list = [110, 9, 89]
        target = 9
        solution = [None, None]
        self.assertListEqual(pair_sum(input_list, target), solution)

if __name__ == '__main__':
    unittest.main()