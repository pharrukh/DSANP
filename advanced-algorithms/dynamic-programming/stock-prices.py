import unittest


# def max_returns(prices):
#     """
#     Calculate maxiumum possible return

#     Args:
#        prices(array): array of prices
#     Returns:
#        int: The maximum profit possible
#     """
#     min_price_index = 0
#     max_price_index = 0
#     min_price = 99999999
#     max_price = 0
#     for i, price in enumerate(prices):
#         if max_price < price and max_price_index <= i:
#             max_price_index = i
#             max_price = price
#         if min_price > price and i <= min_price_index:
#             min_price = price
#             min_price_index = i
#     return (max_price - min_price)

def max_returns(arr):
    min_price_index = 0
    max_price_index = 1
    current_min_price_index = 0
    
    if len(arr) < 2:
        return
    
    for index in range(1, len(arr)):
        # current minimum price
        if arr[index] < arr[current_min_price_index]:
            current_min_price_index = index
            
        # current max profit
        if arr[max_price_index] - arr[min_price_index] < arr[index] - arr[current_min_price_index]:
            max_price_index = index
            min_price_index = current_min_price_index
    max_profit = arr[max_price_index] - arr[min_price_index]
    return max_profit


class Tests(unittest.TestCase):

    def test_1(self):
        prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
        solution = 76
        self.assertEqual(max_returns(prices), solution)

    def test_2(self):
        prices = [54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]
        solution = 66
        self.assertEqual(max_returns(prices), solution)

    def test_3(self):
        prices = [78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]
        solution = 0
        self.assertEqual(max_returns(prices), solution)


if __name__ == '__main__':
    unittest.main()
