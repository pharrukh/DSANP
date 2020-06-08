import unittest
import math

def sort_a_little_bit(items, start_index, end_index):
    left_index = start_index
    partition_index = end_index
    partition = items[end_index]

    while left_index != partition_index:
        item = items[left_index]

        if item <= partition:
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

def break_into_groups(Arr, num):
    group_size = math.ceil(len(Arr)/num)
    new_arr = []
    cur_group = []
    for i, a in enumerate(Arr):
        cur_group.append(a)
        if len(cur_group) == group_size or i == len(Arr) - 1:
            new_arr.append(cur_group)
            cur_group = []
    return new_arr

def partition(Arr, pivot):
    Arr_Less_P = []
    Arr_Equal_P = []
    Arr_More_P = []
    for a in Arr:
        if a < pivot:
            Arr_Less_P.append(a)
        elif a == pivot:
            Arr_Equal_P.append(a)
        else:
            Arr_More_P.append(a)
    return (Arr_Less_P, Arr_Equal_P, Arr_More_P)

def get_median(Arr):
    return Arr[len(Arr)//2]

def fastSelect(Arr, k):

    G = break_into_groups(Arr, 5)
    S = set()
    for group in G:
        quicksort(group)
        median = get_median(group)
        S.add(median)
    pivot = fastSelect(list(S), len(Arr)//10) # not sure which devision to do
    Arr_Less_P, Arr_Equal_P, Arr_More_P = partition(Arr, pivot)
    if k <= len(Arr_Equal_P):
        return fastSelect(Arr_Less_P, k)
    elif k > (len(Arr_Less_P) + len(Arr_Equal_P)):
        return fastSelect(Arr_More_P, (k-len(Arr_Less_P)-len(Arr_Equal_P)))
    return pivot

def fastSelect_v2(Arr, k):                         # k is an index
    n = len(Arr)                                # length of the original array
    
    if(k>0 and k <= n):                         # k should be a valid index         
        # Helper variables
        setOfMedians = []
        Arr_Less_P = []
        Arr_Equal_P = []
        Arr_More_P = []
        i = 0
        
        # Step 1 - Break Arr into groups of size 5
        # Step 2 - For each group, sort and find median (middle). Add the median to setOfMedians
        while (i < n // 5):                     # n//5 gives the integer quotient of the division 
            median = findMedian(Arr, 5*i, 5)    # find median of each group of size 5
            setOfMedians.append(median)         
            i += 1

        # If n is not a multiple of 5, then a last group with size = n % 5 will be formed
        if (5*i < n): 
            median = findMedian(Arr, 5*i, n % 5)
            setOfMedians.append(median)
        
        # Step 3 - Find the median of setOfMedians
        if (len(setOfMedians) == 1):            # Base case for this task
            pivot = setOfMedians[0]
        elif (len(setOfMedians)>1):
            pivot = fastSelect(setOfMedians, (len(setOfMedians)//2))
        
        # Step 4 - Partition the original Arr into three sub-arrays
        for element in Arr:
            if (element<pivot):
                Arr_Less_P.append(element)
            elif (element>pivot):
                Arr_More_P.append(element)
            else:
                Arr_Equal_P.append(element)
        
        # Step 5 - Recurse based on the sizes of the three sub-arrays
        if (k <= len(Arr_Less_P)):
            return fastSelect(Arr_Less_P, k)
        
        elif (k > (len(Arr_Less_P) + len(Arr_Equal_P))):
            return fastSelect(Arr_More_P, (k - len(Arr_Less_P) - len(Arr_Equal_P)))
            
        else:
            return pivot     

# Helper function
def findMedian(Arr, start, size): 
    myList = [] 
    for i in range(start, start + size): 
        myList.append(Arr[i]) 
          
    # Sort the array  
    myList.sort() 
  
    # Return the middle element 
    return myList[size // 2] 

class Tests(unittest.TestCase):

    def test_break_into_groups_0(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        solution = [[1 , 2], [3, 4], [5, 6], [7, 8], [9, 10]]
        self.assertListEqual(break_into_groups(arr, 5), solution)

    def test_break_into_groups_1(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        solution = [[1 , 2, 3], [4, 5, 6], [7, 8, 9], [10, 11]]
        self.assertListEqual(break_into_groups(arr, 5), solution)

    def test_break_into_groups_2(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        solution = [[1, 2], [3, 4], [5, 6], [7]]
        self.assertListEqual(break_into_groups(arr, 5), solution)

    def test_partition_0(self):
        arr = [1,2]
        solution = ([1], [2], [])
        self.assertTupleEqual(partition(arr, 2), solution)

    def test_partition_1(self):
        arr = [1,2,3,4,5,6,7,8,9,10]
        solution = ([1,2,3,4], [5], [6,7,8,9,10])
        self.assertTupleEqual(partition(arr, 5), solution)

    def test_0(self):
        Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
        k = 5
        self.assertEqual(fastSelect(Arr, k), 12)        

    def test_1(self):
        Arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
        k = 5
        result = fastSelect(Arr, k)
        self.assertEqual(result, 11)        

    def test_2(self):
        Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
        k = 10
        result = fastSelect(Arr, k)
        self.assertEqual(result, 99)        


if __name__ == '__main__':
    unittest.main()