import unittest


def swap(arr, a, b):
    temp = arr[b]
    arr[b] = arr[a]
    arr[a] = temp


def sort_012(arr):
    """

    Args:
       arr(list): List to be sorted
    """
    length = len(arr)
    zero = 0
    front = 0
    two = length - 1
    while front <= two:
        if arr[front] == 0:
            swap(arr, front, zero)
            front += 1
            zero += 1
        elif arr[front] == 2:
            swap(arr, front, two)
            two -= 1
        else:
            front += 1


class Tests(unittest.TestCase):

    def test_0(self):
        arr = [2, 0, 1]
        sol = [0, 1, 2]
        sort_012(arr)
        self.assertListEqual(arr, sol)

    def test_1(self):
        arr = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
        sol = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
        sort_012(arr)
        self.assertListEqual(arr, sol)

    def test_2(self):
        arr = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2,
               2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
        sol = [0, 0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 1, 1, 1, 1, 1, 1, 2, 2,  2,  2, 2,
               2, 2, 2,  2]
        sort_012(arr)
        self.assertListEqual(arr, sol)

    def test_3(self):
        arr = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
        sol = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
        sort_012(arr)
        self.assertListEqual(arr, sol)


if __name__ == '__main__':
    unittest.main()
