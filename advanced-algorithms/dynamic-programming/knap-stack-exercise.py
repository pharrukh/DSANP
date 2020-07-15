import unittest
import collections

# An item can be represented as a namedtuple
Item = collections.namedtuple('Item', ['weight', 'value'])
# Naive Approach based on Recursion
def knapsack_max_value_naive(knapsack_max_weight, items):
    lastIndex = len(items) - 1
    return knapsack_recursive(knapsack_max_weight, items, lastIndex)

def knapsack_recursive(capacity, items, lastIndex):
    # Base case
    if (capacity <= 0) or (lastIndex < 0):
        return 0

    # Put the item in the knapsack
    valueA = 0
    if (items[lastIndex].weight <= capacity):
        valueA = items[lastIndex].value + knapsack_recursive(
            capacity - items[lastIndex].weight, items, lastIndex - 1)

    # Do not put the item in the knapsack
    valueB = knapsack_recursive(capacity, items, lastIndex - 1)

    # Pick the maximum of the two results
    result = max(valueA, valueB)

    return result

def knapsack_max_value(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack.
    """
    lookup_table = [0] * (knapsack_max_weight + 1)
    for weight, value in items:
        for capacity in reversed(range(knapsack_max_weight + 1)):
            if weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - weight] + value)
    return lookup_table[-1]

class Tests(unittest.TestCase):

    def test_1(self):
        answer = 14
        knapsack_max_weight = 15
        items = [Item(10, 7), Item(9, 8), Item(5, 6)]
        self.assertEqual(knapsack_max_value(
            knapsack_max_weight, items), answer)

    def test_2(self):
        answer = 13
        knapsack_max_weight = 25
        items = [Item(10, 2), Item(29, 10), Item(5, 7),
                Item(5, 3), Item(5, 1), Item(24, 12)]
        self.assertEqual(knapsack_max_value(
            knapsack_max_weight, items), answer)

if __name__ == '__main__':
    unittest.main()
