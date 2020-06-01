def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)

def find_first(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return None
    while True:
        if source[index] != target:
            return index + 1
        if index == 0:
            return 0
        index -= 1
    return index

def find_last(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return None
    max_len = len(source) - 1
    while True:
        if source[index] != target:
            return index - 1
        if index == max_len:
            return max_len
        index += 1
    return index

def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary 
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """
    index = recursive_binary_search(number, arr)
    if index == None:
        return [-1, -1]
    return [find_first(number, arr), find_last(number, arr)]

print(first_and_last_index([1,1,1,1,1,1, 2], 1))
print(first_and_last_index([1,1,1,1,1,1, 2], 2))
print(first_and_last_index([1,1,1,1,1,1, 2], 3))
print(first_and_last_index([1,2,3,4,5,6,7,7,8], 7))
print(first_and_last_index([1,2,3,4,5,6,7,7,8], 5))
print(first_and_last_index([1], 1))