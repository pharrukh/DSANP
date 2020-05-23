import unittest

class Node:

    def __init__(self, value, key):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return '({})'.format(self.value)

class DoubleLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def set(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
    
    def remove_last(self):
        if not self.head:
            return
        self.tail.prev.next = None
        self.tail = self.tail.prev
    
    def move_top(self, node):
        if node is self.head:
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.tail:
            self.remove_last()
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node

    def __str__(self):
        string = ''
        node = self.head
        while True:
            string += '({})->'.format(str(node.value))
            if not node.next:
                break
            node = node.next
        return string

class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = dict()
        self.list = DoubleLinkedList()
        self.size = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.dict:
            node = self.dict[key]
            self.list.move_top(node)
            return node.value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.dict and value == self.dict[key].value:
            existing_node = self.dict[key]
            self.list.move_top(existing_node)
        else:
            node = Node(value, key)
            if self.size == self.capacity:
                last_key = self.list.tail.key
                del self.dict[last_key]
                self.list.remove_last()
                self.size -= 1
            self.dict[key] = node
            self.list.set(node)
            self.size += 1


    def __str__(self):
        string = ''
        for key in self.dict:
            string += '[{}]:{};'.format(str(key), str(self.dict[key]))
        return string

class LRU_CacheTests(unittest.TestCase):

    def test_all_methods_as_given(self):
        our_cache = LRU_Cache(5)
        self.assertEqual(str(our_cache), '')
        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)
        self.assertEqual(str(our_cache), '[1]:(1);[2]:(2);[3]:(3);[4]:(4);')

        self.assertEqual(our_cache.get(1), 1)       # returns 1
        self.assertEqual(our_cache.get(2), 2)       # returns 2
        self.assertEqual(our_cache.get(9), -1)      # returns -1 because 9 is not present in the cache

        our_cache.set(5, 5) 
        our_cache.set(6, 6)

        self.assertEqual(str(our_cache), '[1]:(1);[2]:(2);[4]:(4);[5]:(5);[6]:(6);')
        self.assertEqual(our_cache.get(3), -1)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    def test_all_methods_as_complex(self):
        our_cache = LRU_Cache(5)
        self.assertEqual(str(our_cache), '')
        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)
        self.assertEqual(str(our_cache), '[1]:(1);[2]:(2);[3]:(3);[4]:(4);')
        self.assertEqual(str(our_cache.list), '(4)->(3)->(2)->(1)->')

        self.assertEqual(our_cache.get(1), 1)       # returns 1
        self.assertEqual(str(our_cache.list), '(1)->(4)->(3)->(2)->')
        self.assertEqual(our_cache.get(2), 2)       # returns 2
        self.assertEqual(str(our_cache.list), '(2)->(1)->(4)->(3)->')
        self.assertEqual(our_cache.get(9), -1)      # returns -1 because 9 is not present in the cache

        our_cache.set(5, 5)
        self.assertEqual(str(our_cache.list), '(5)->(2)->(1)->(4)->(3)->')
        our_cache.set(6, 6)
        self.assertEqual(str(our_cache.list), '(6)->(5)->(2)->(1)->(4)->')

        self.assertEqual(str(our_cache), '[1]:(1);[2]:(2);[4]:(4);[5]:(5);[6]:(6);')
        self.assertEqual(our_cache.get(3), -1)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
        
        our_cache.set(100, 100)
        self.assertEqual(str(our_cache.list), '(100)->(6)->(5)->(2)->(1)->')
        our_cache.set(123, 123)
        self.assertEqual(str(our_cache.list), '(123)->(100)->(6)->(5)->(2)->')
        our_cache.set(46, 46)
        self.assertEqual(str(our_cache.list), '(46)->(123)->(100)->(6)->(5)->')
        our_cache.set(90, 90)
        self.assertEqual(str(our_cache.list), '(90)->(46)->(123)->(100)->(6)->')
        our_cache.set(190, 190)
        self.assertEqual(str(our_cache.list), '(190)->(90)->(46)->(123)->(100)->')
        self.assertEqual(str(our_cache), '[100]:(100);[123]:(123);[46]:(46);[90]:(90);[190]:(190);')

        our_cache.set(100, 100)
        self.assertEqual(str(our_cache.list), '(100)->(190)->(90)->(46)->(123)->')
        self.assertEqual(str(our_cache), '[100]:(100);[123]:(123);[46]:(46);[90]:(90);[190]:(190);')
        our_cache.set(100, 100)
        self.assertEqual(str(our_cache.list), '(100)->(190)->(90)->(46)->(123)->')
        our_cache.set(190, 190)
        self.assertEqual(str(our_cache.list), '(190)->(100)->(90)->(46)->(123)->')
        self.assertEqual(our_cache.get(124), -1)
        self.assertEqual(our_cache.get(123), 123)
        self.assertEqual(str(our_cache.list), '(123)->(190)->(100)->(90)->(46)->')
        self.assertEqual(our_cache.get(100), 100)
        self.assertEqual(str(our_cache.list), '(100)->(123)->(190)->(90)->(46)->')
        self.assertEqual(our_cache.get(90), 90)
        self.assertEqual(str(our_cache.list), '(90)->(100)->(123)->(190)->(46)->')

    def test__max_size(self):
        our_cache=LRU_Cache(3)
        our_cache.set(1,1)
        our_cache.set(2,2)
        our_cache.set(3,3)
        our_cache.set(4,4)
        self.assertEqual(our_cache.get(4), 4)   # Expected Value = 4
        self.assertEqual(our_cache.get(1), -1)   # Expected Value = -1
        our_cache.set(2,4)
        self.assertEqual(our_cache.get(2), 4)   # Expected Value = 4 Your Output = 2

if __name__ == '__main__':
    unittest.main()