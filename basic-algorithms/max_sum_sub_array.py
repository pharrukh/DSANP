import unittest
import math

# def maxCrossingSum(arr, start, mid, stop):
#     leftMaxSum = 0
#     rightMaxSum = 0



#     return leftMaxSum + rightMaxSum

# def maxSubArrayRecursive(arr, start, stop):
#     if (start==stop):
#         return arr[start]

# #       2. Calculate mid index       constant
#     mid = (start+stop)//2

# #       3. L = maxSubArrayRecursive(arr, start, mid)       T( 𝑛2 )
#     left = maxSubArrayRecursive(arr, start, mid)
# #       4. R = maxSubArrayRecursive(arr, mid+1, stop)       T( 𝑛2 )
#     right = maxSubArrayRecursive(arr, mid+1, stop)
# #       5. C = maxCrossingSum(arr, start, mid, stop)         Θ(𝑛) 

# #       6. return max(C, max(L,R)) 

def maxSubArray(arr):
    best_sum = 0
    current_sum = 0
    for x in arr:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
        print(x, current_sum, best_sum)
    return best_sum


class Tests(unittest.TestCase):

    def test_0(self):
        arr = [-2, 7, -6, 3, 1, -4, 5, 7]
        self.assertEqual(maxSubArray(arr), 13)
    
    def test_1(self):
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(maxSubArray(arr), 6)

    def test_2(self):
        arr = [-4, 14, -6, 7]
        self.assertEqual(maxSubArray(arr), 15)
    
    def test_3(self):
        arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
        self.assertEqual(maxSubArray(arr), 10)

if __name__ == '__main__':
    unittest.main()