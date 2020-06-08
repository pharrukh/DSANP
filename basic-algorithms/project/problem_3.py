import unittest

def sort_a_little_bit(items, start_index, end_index):
    left_index = start_index
    partition_index = end_index
    partition = items[end_index]

    while left_index != partition_index:
        item = items[left_index]

        if item >= partition:
            left_index += 1
            continue

        items[left_index] = items[partition_index-1]
        items[partition_index-1] = partition
        items[partition_index] = item

        partition_index-=1

    return partition_index

def sort_all(items, start_index, end_index):
    if start_index >= end_index:
        return
    
    partition_index = sort_a_little_bit(items, start_index, end_index)
    sort_all(items, start_index, partition_index-1)
    sort_all(items, partition_index+1, end_index)

def quicksort(items):
    sort_all(items, 0, len(items)-1)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    length = len(input_list)
    if length < 2:
        raise Exception("'input_list' must have more than two elements.")
    quicksort(input_list)
    num_one_str = str(input_list[0])
    num_two_str = str(input_list[1])
    for i in range(2, len(input_list)):
        el = input_list[i]
        if i % 2 == 0:
            num_one_str += str(el)
        else:
            num_two_str += str(el)
    return (int(num_one_str), int(num_two_str))


class Tests(unittest.TestCase):

    def test_0(self):
        coll = [1, 2, 3, 4, 5]
        a,b = rearrange_digits(coll)
        self.assertEqual(a+b, 542 + 31)
        self.assertEqual(a+b, 531 + 42)
    def test_1(self):
        coll = [4, 6, 2, 5, 9, 8]
        a,b = rearrange_digits(coll)
        self.assertEqual(a+b, 964 + 852)
        self.assertEqual(a+b, 952 + 864)
    def test_2(self):
        coll = [1,2,3,4,5,6,7,8,9,10]
        a,b = rearrange_digits(coll)
        self.assertEqual(a+b, 108642 + 97531)
if __name__ == '__main__':
    unittest.main()