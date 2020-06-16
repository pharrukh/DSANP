# Max and Min in a Unsorted Array
import random
import unittest


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_int = ints[0]
    max_int = ints[0]
    for el in ints:
        if min_int > el:
            min_int = el
        if max_int < el:
            max_int = el
    return (min_int, max_int)


class Tests(unittest.TestCase):

    def test_0(self):
        l = [0]
        self.assertEqual(get_min_max(l), (0, 0) )

    def test_1(self):
        l = [1, 0]
        self.assertEqual(get_min_max(l), (0, 1) )

    def test_random_shuffle(self):
        for _ in range(100):
            l = [i for i in range(0, 1001)]  # a list containing 0 - 1000
            random.shuffle(l)
            self.assertEqual(get_min_max(l), (0, 1000) )

if __name__ == '__main__':
    unittest.main()
