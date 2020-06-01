import unittest

def count_inversions(arr):
    start_index = 0
    end_index = len(arr) - 1
    output = inversion_count_func(arr, start_index, end_index)
    return output


# exactly as the normal merge sort
# here we use three pointers: start_index, mid_index and end_index
def inversion_count_func(arr, start_index, end_index):
    if start_index >= end_index:
        return 0

    mid_index = start_index + (end_index - start_index) // 2
    
    # find number of inversions in left-half
    left_answer = inversion_count_func(arr, start_index, mid_index)
    
    # find number of inversions in right-half
    right_answer = inversion_count_func(arr, mid_index + 1, end_index)

    output = left_answer + right_answer
    
    # merge two sorted halves and count inversions while merging
    output += merge_two_sorted_halves(arr, start_index, mid_index, mid_index + 1, end_index)
    return output

"""
    Four pointers are used: start_one, end_one, start_two, end_two

"""
def merge_two_sorted_halves(arr, start_one, end_one, start_two, end_two):
    count = 0
    left_index = start_one
    right_index = start_two

    output_length = (end_two - start_two + 1) + (end_one - start_one + 1)
    output_list = [0 for _ in range(output_length)]
    index = 0

    while index < output_length:
        # if left <= right, it's not an inversion
        if arr[left_index] <= arr[right_index]:
            output_list[index] = arr[left_index]
            left_index += 1

        else:
            count = count + (end_one - left_index + 1)           # left > right hence it's an inversion
            output_list[index] = arr[right_index]
            right_index += 1

        index = index + 1


        # when one section (left or rigth) was already iterated
        # just put all values from one collection to another
        if left_index > end_one:
            for i in range(right_index, end_two + 1):
                output_list[index] = arr[i]
                index += 1
            break

        elif right_index > end_two:
            for i in range(left_index, end_one + 1):
                output_list[index] = arr[i]
                index += 1
            break

    print(arr)
    print(output_list)
    # order only small section that is for the current function call
    index = start_one
    for i in range(output_length):
        arr[index] = output_list[i]
        index += 1
    print(arr)
    return count

class Tests(unittest.TestCase):

    def test_0(self):
        arr = [0,1]
        expected_count = 0
        self.assertEqual(count_inversions(arr), expected_count)

    def test_1(self):
        arr = [2,1]
        expected_count = 1
        self.assertEqual(count_inversions(arr), expected_count)

    def test_2(self):
        arr = [3, 1, 2, 4]
        expected_count = 2
        self.assertEqual(count_inversions(arr), expected_count)

    def test_3(self):
        arr = [7, 5, 3, 1]
        expected_count = 6
        self.assertEqual(count_inversions(arr), expected_count)

    def test_4(self):
        arr = [7, 5, 3]
        expected_count = 3
        self.assertEqual(count_inversions(arr), expected_count)

    def test_5(self):
        arr = [2, 5, 1, 3, 4]
        expected_count = 4
        self.assertEqual(count_inversions(arr), expected_count)

    def test_6(self):
        arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
        expected_count = 26
        self.assertEqual(count_inversions(arr), expected_count)

    def test_7(self):
        arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
        expected_count = 2
        self.assertEqual(count_inversions(arr), expected_count)

if __name__ == '__main__':
    unittest.main()