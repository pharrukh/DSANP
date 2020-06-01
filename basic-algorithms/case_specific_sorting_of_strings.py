import unittest

def is_less(a,b):
    return ord(a) < ord(b)

def merge(arr1, arr2):
    i = 0
    j = 0

    l = []
    while True:
        if i == len(arr1):
            if j == len(arr2):
                return l
            l.append(arr2[j])
            j += 1
        elif j == len(arr2):
            if i == len(arr1):
                return l
            l.append(arr1[i])
            i += 1
        elif is_less(arr1[i], arr2[j]):
            l.append(arr1[i])
            i += 1
        else:
            l.append(arr2[j])
            j += 1

def merge_sort(arr):
    # if it is one return
    length = len(arr)
    if length <= 1:
        return arr
    # split the collection while it is more than one
    # if number of elements is odd, leave the first element ??
    # split the collection into two
    mid = length // 2
    left = merge_sort(arr[mid:])
    right = merge_sort(arr[:mid])
    # merge two ordered collections into one

    # return ordered collection
    return merge(left, right)

def get_next_lowercase_char_index(arr, base_index):
    next_lowercase_char_index = base_index + 1
    while next_lowercase_char_index < len(arr):
        if arr[next_lowercase_char_index].islower():
            return next_lowercase_char_index
        next_lowercase_char_index += 1

def get_next_uppercase_char_index(arr, base_index):
    next_uppercase_char_index = base_index + 1
    while next_uppercase_char_index < len(arr):
        if not arr[next_uppercase_char_index].islower():
            return next_uppercase_char_index
        next_uppercase_char_index += 1

def case_sort(string):
    """
    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output list
        else:
            pick upper-case character from sorted string to place in output list
    
    Note: You can use Python's inbuilt ord() function to find the ASCII value of a character
    """
    sorted_string = merge_sort(string)
    output_string = ''
    n = get_next_lowercase_char_index(sorted_string, -1)
    m = get_next_uppercase_char_index(sorted_string, -1)
    for i in range(len(string)):
        char = string[i]
        if char.islower():
            next_lowercase_char = sorted_string[n]
            output_string += next_lowercase_char
            n = get_next_lowercase_char_index(sorted_string, n)
        else:
            next_uppercase_char = sorted_string[m]
            output_string += next_uppercase_char
            m = get_next_uppercase_char_index(sorted_string, m)
    return output_string
    
"""
def case_sort(string):
    upper_ch_index = 0
    lower_ch_index = 0
    
    sorted_string = sorted(string)
    for index, character in enumerate(sorted_string):
        # check if character is lower-case
        ascii_int = ord(character)
        if 97 <= ascii_int <= 122:       # ASCII value of a = 97 & ASCII value of z = 122
            lower_ch_index = index
            break
            
    output = list()
    for character in string:
        ascii_int = ord(character)
        # if character is lower case pick next lower_case character
        if 97 <= ascii_int <= 122:
            output.append(sorted_string[lower_ch_index])
            lower_ch_index += 1
        else:
            output.append(sorted_string[upper_ch_index])
            upper_ch_index += 1
    return "".join(output)
"""


class Tests(unittest.TestCase):

    def test_0(self):
        test_string = 'fedRTSersUXJ'
        solution = "deeJRSfrsTUX"
        self.assertEquals(case_sort(test_string), solution)

    def test_1(self):
        test_string = "defRTSersUXI"
        solution = "deeIRSfrsTUX"
        self.assertEquals(case_sort(test_string), solution)

    def test_2(self):
        test_string = "aAbBcCdDfFgG"
        solution = "aAbBcCdDfFgG"
        self.assertEquals(case_sort(test_string), solution)

    def test_3(self):
        test_string = "ZzYyXx"
        solution = "XxYyZz"
        self.assertEquals(case_sort(test_string), solution)

if __name__ == '__main__':
    unittest.main()