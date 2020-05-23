import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):
        self.size += 1
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        

def fill_map(map, llist):
    node = llist.head
    while True:
        value = node.value
        if value not in map.keys():
            map[value] = value
        if not node.next:
            break
        node = node.next
    return map
    

def union(llist_1, llist_2):

    if llist_1.size == 0 and llist_2.size == 0:
        return LinkedList()
    if llist_1.size == 0:
        return llist_2
    if llist_2.size == 0:
        return llist_1

    map = dict()
    fill_map(map, llist_1)
    fill_map(map, llist_2)
    result_list = LinkedList()
    for value in map.keys():
        result_list.append(value)
    return result_list


def intersection(llist_1, llist_2):
    if llist_1.size == 0 or llist_2.size == 0:
        return LinkedList()

    map1 = dict()
    fill_map(map1, llist_1)
    map2 = dict()
    fill_map(map2, llist_2)
    result_list = LinkedList()
    for val in map1.keys():
        if val in map2.keys():
            result_list.append(val)
    return result_list

class problem_6_tests(unittest.TestCase):

    def _run_test(self, l1, l2, expected_union, expected_intersection):
        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        for i in l1:
            linked_list_1.append(i)

        for i in l2:
            linked_list_2.append(i)
        
        actual_union_list = union(linked_list_1,linked_list_2)
        self.assertEqual(str(actual_union_list), expected_union)
        actual_intersection_list = intersection(linked_list_1,linked_list_2)
        self.assertEquals(str(actual_intersection_list), expected_intersection)      

    def test1(self):
        l1 = [3,2,4,35,6,65,6,4,3,21]
        l2 = [6,32,4,9,6,1,11,21,1]
        union = '3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> '
        intersection = '4 -> 6 -> 21 -> '
        self._run_test(l1, l2, union, intersection)
        
    def test2(self):
        l1 = [3,2,4,35,6,65,6,4,3,23]
        l2 = [1,7,8,9,11,21,1]
        union = '3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> '
        intersection = ''
        self._run_test(l1, l2, union, intersection)

    def test3(self):
        l1 = []
        l2 = []
        union = ''
        intersection = ''
        self._run_test(l1, l2, union, intersection)

    def test4(self):
        l1 = [1]
        l2 = []
        union = '1 -> '
        intersection = ''
        self._run_test(l1, l2, union, intersection)

    def test5(self):
        l1 = []
        l2 = [1]
        union = '1 -> '
        intersection = ''
        self._run_test(l1, l2, union, intersection)

    def test6(self):
        l1 = [1]
        l2 = [1]
        union = '1 -> '
        intersection = '1 -> '
        self._run_test(l1, l2, union, intersection)

    def test7(self):
        l1 = [1,2,3,4,5,6,7,8]
        l2 = [1,2,3,4,5,6,7,8]
        union = '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> '
        intersection = '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> '
        self._run_test(l1, l2, union, intersection)

    def test8(self):
        l1 = [1,1,1,1,1,1,1,1]
        l2 = [2,2,2,2,2,2,2,2]
        union = '1 -> 2 -> '
        intersection = ''
        self._run_test(l1, l2, union, intersection)

    def test9(self):
        l1 = [1,2,3,4,2,2,2,2,3,3,3,5,5,5]
        l2 = [2,3,5]
        union = '1 -> 2 -> 3 -> 4 -> 5 -> '
        intersection = '2 -> 3 -> 5 -> '
        self._run_test(l1, l2, union, intersection)

if __name__ == '__main__':
    unittest.main()


