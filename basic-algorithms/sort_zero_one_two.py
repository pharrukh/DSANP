import unittest

def swap(arr, i ,j):
    arr[i], arr[j] = arr[j], arr[i]

def sort_012(arr):
    zero_pointer = 0
    two_pointer = len(arr) - 1
    while zero_pointer != two_pointer:
        if arr[zero_pointer] == 0:
            zero_pointer += 1
        elif arr[two_pointer] == 2:
            two_pointer -= 1
        elif arr[zero_pointer] == 2 and arr[two_pointer] != 2:
            swap(arr, zero_pointer, two_pointer)
            two_pointer -= 1
        elif arr[zero_pointer] != 0 and arr[two_pointer] == 0:
            swap(arr, zero_pointer, two_pointer)
            zero_pointer += 1

class Tests(unittest.TestCase):

    def test_0(self):
        test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
        solution = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
        sort_012(test_case)
        self.assertListEqual(test_case, solution)

    def test_1(self):
        test_case = test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
        solution = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        sort_012(test_case)
        self.assertListEqual(test_case, solution)

    def test_2(self):
        test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
        solution = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
        sort_012(test_case)
        self.assertListEqual(test_case, solution)

    def test_3(self):
        test_case = [0, 0, 0, 2, 2, 1, 1, 1, 2, 2, 2]
        solution = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
        sort_012(test_case)
        self.assertListEqual(test_case, solution)

    def test_4(self):
        test_case = [1, 2, 0]
        solution = [0, 1, 2]
        sort_012(test_case)
        self.assertListEqual(test_case, solution)

    def test_5(self):
        test_case = [2, 1, 2, 0]
        solution = [0, 1, 2, 2]
        sort_012(test_case)
        self.assertListEqual(test_case, solution)

    def test_6(self):
        test_case = [2, 2, 1, 0]
        solution = [0, 1, 2, 2]
        sort_012(test_case)
        self.assertListEqual(test_case, solution)

if __name__ == '__main__':
    unittest.main()