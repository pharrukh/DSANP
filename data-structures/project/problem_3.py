import unittest
import sys

class Node:
    def __init__(self, value, letter = None):
        self.letter = letter
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root

class MinPriorityQueue:

    def __init__(self, max_size):
        self.arr = [None for i in range(max_size+1)]
        self.size = 0

    def get_coll(self):
        return [None if node is None else node.value for node in self.arr]
    
    def is_empty(self):
        return self.size == 0

    def insert(self, item):
        self.size += 1
        index = self.size
        self.arr[index] = item
        self._swim(index)

    def del_min(self):
        if self.is_empty():
            return None
        min = self.arr[1]
        self._exchange(1, self.size)
        self.size -= 1
        self.arr[self.size+1] = None
        self._sink(1)
        return min

    def _is_more(self, i, j):
        return self.arr[i].value > self.arr[j].value

    def _exchange(self, i, j):
        t = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = t

    def _swim(self, k):
        while k>1 and self._is_more(k//2, k):
            self._exchange(k//2, k)
            k = k//2

    def _sink(self, k):
        while 2*k <= self.size:
            j = k*2
            if j < self.size and self._is_more(j, j+1):
                j += 1
            if not self._is_more(k, j):
                break
            self._exchange(k, j)
            k = j

def build_frequency_map(string):
    map = dict()
    for char in string:
        if char not in map:
            map[char] = 1
        else:
            map[char] += 1
    return map

def convert_to_pq(map):
    min_pq = MinPriorityQueue(len(map))
    for letter, value in map.items():
        node = Node(value, letter)
        min_pq.insert(node)
    return min_pq

def build_huffman_tree(pq):
    if pq.is_empty() or pq.size == 1:
        return pq

    while pq.size > 1:
        node1 = pq.del_min()
        node2 = pq.del_min()
        node = Node(node1.value + node2.value)
        node.left = node1
        node.right = node2
        pq.insert(node)
    
    return pq.del_min()



def build_code_map(root):
    map = dict()

    def traverse(node, prefix):
        if node:
            # traverse left subtree
            traverse(node.left, prefix + '0')
            
            if not node.left and not node.right:
                map[node.letter] = prefix

            # traverse right sub-tree
            traverse(node.right, prefix + '1')

    traverse(root, '')     
    return map

def encode(map, string):
    new_string = string
    for letter, code in map.items():
        new_string = new_string.replace(letter, code)
    return new_string

def huffman_encoding(data):
    if not data or data == '':
        raise Exception('Nothing to encode')
    map = build_frequency_map(data)
    mpq = convert_to_pq(map)
    root = build_huffman_tree(mpq)
    code_map = build_code_map(root)
    encoded_string = encode(code_map, data)
    return (encoded_string, Tree(root))

def decode_recursive(encoded_string, decoded_string, root, node, i):
    if node.letter:
        decoded_string += node.letter

    if i == len(encoded_string):
        return decoded_string

    if encoded_string[i] == '0':
        if node.left:
            return decode_recursive(encoded_string, decoded_string, root, node.left, i+1)
    elif encoded_string[i] == '1':
        if node.right:
            return decode_recursive(encoded_string, decoded_string, root, node.right, i+1)
    
    return decode_recursive(encoded_string, decoded_string, root,  root, i)

def huffman_decoding(data,tree):
    return decode_recursive(data, '', tree.root, tree.root, 0)
        


class problem_3_tests(unittest.TestCase):

    def test1(self):
        map1 = build_frequency_map('AAAAAAABBBCCCCCCCDDEEEEEE')
        self.assertEqual(map1, {'A': 7, 'B': 3, 'C': 7, 'D': 2, 'E': 6})
        map2 = build_frequency_map('AAAAAAACCDDEFFFFFXXXX')
        self.assertEqual(map2, {'A': 7, 'C': 2, 'D': 2, 'E': 1, 'F': 5, 'X': 4})

    def test2(self):
        mpq = convert_to_pq({'A': 7, 'B': 3, 'C': 7, 'D': 2, 'E': 6})
        self.assertEqual(mpq.get_coll(), [None, 2, 3, 7, 7, 6])
        mpq = convert_to_pq({'A': 7, 'C': 2, 'D': 2, 'E': 1, 'F': 5, 'X': 4})
        self.assertEqual(mpq.get_coll(), [None, 1, 2, 2, 7, 5, 4])

    def test3(self):
        mpq = convert_to_pq({'A': 7, 'B': 3, 'C': 7, 'D': 2, 'E': 6})
        root = build_huffman_tree(mpq)
        self.assertEqual(root.value, 25)
        l1 = root.left
        self.assertEqual(l1.value, 11)
        r1 = root.right
        self.assertEqual(r1.value, 14)
        l2 = l1.left
        self.assertEqual(l2.value, 5)
        r2 = l1.right
        self.assertEqual(r2.value, 6)
        self.assertEqual(r2.letter, 'E')

        l2_2 = r1.left
        self.assertEqual(l2_2.value, 7)
        self.assertEqual(l2_2.letter, 'C')
        r2_2 = r1.right
        self.assertEqual(r2_2.value, 7)
        self.assertEqual(r2_2.letter, 'A')

        l3 = l2.left
        self.assertEqual(l3.value, 2)
        self.assertEqual(l3.letter, 'D')
        r3 = l2.right
        self.assertEqual(r3.value, 3)
        self.assertEqual(r3.letter, 'B')

    def test4(self):
        mpq = convert_to_pq({'A': 7, 'B': 3, 'C': 7, 'D': 2, 'E': 6})
        root = build_huffman_tree(mpq)
        code_map = build_code_map(root)
        self.assertEqual(code_map, {'D': '000', 'B': '001', 'E': '01', 'C': '10', 'A': '11'})

        mpq2 = convert_to_pq({'A': 7, 'C': 2, 'D': 2, 'E': 1, 'F': 5, 'X': 4})
        root2 = build_huffman_tree(mpq2)
        code_map2 = build_code_map(root2)
        self.assertEqual(code_map2, {'A': '11', 'C': '0111', 'D': '010', 'E': '0110', 'F': '10', 'X': '00'})

    def test5(self):
        new_string = encode({'D': '000', 'B': '001', 'E': '01', 'C': '10', 'A': '11'}, 'AAAAAAABBBCCCCCCCDDEEEEEE')
        self.assertEqual(new_string, '1111111111111100100100110101010101010000000010101010101')


    def test6(self):
        encoded_data, tree = huffman_encoding('AAAAAAABBBCCCCCCCDDEEEEEE')
        root = tree.root
        self.assertEqual(root.value, 25)
        l1 = root.left
        self.assertEqual(l1.value, 11)
        r1 = root.right
        self.assertEqual(r1.value, 14)
        l2 = l1.left
        self.assertEqual(l2.value, 5)
        r2 = l1.right
        self.assertEqual(r2.value, 6)
        self.assertEqual(r2.letter, 'E')

        l2_2 = r1.left
        self.assertEqual(l2_2.value, 7)
        self.assertEqual(l2_2.letter, 'C')
        r2_2 = r1.right
        self.assertEqual(r2_2.value, 7)
        self.assertEqual(r2_2.letter, 'A')

        l3 = l2.left
        self.assertEqual(l3.value, 2)
        self.assertEqual(l3.letter, 'D')
        r3 = l2.right
        self.assertEqual(r3.value, 3)
        self.assertEqual(r3.letter, 'B')
        self.assertEqual(encoded_data, '1111111111111100100100110101010101010000000010101010101')

    def test7(self):
        root = Node(2)
        root.left = Node(1, 'A')
        root.right = Node(1, 'B')
        tree = Tree(root)
        decoded_data = huffman_decoding('01', tree)
        self.assertEqual(decoded_data, 'AB')

    def test8(self):
        original_string = 'AAAAAAABBBCCCCCCCDDEEEEEE'
        encoded_data, tree = huffman_encoding(original_string)
        decoded_data = huffman_decoding(encoded_data, tree)
        self.assertEqual(decoded_data, original_string)

    def test9(self):
        original_string = ''
        self.assertRaises(Exception, huffman_encoding, original_string)

if __name__ == '__main__':
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    unittest.main()