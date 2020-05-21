class Node:

    def __init__(self, value):
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
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.tail:
            self.remove_last()
        self.head.prev = node
        node.next = self.head
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


import unittest

class OrderedListTests(unittest.TestCase):

    def test_adding_nodes(self):
        dll = DoubleLinkedList()
        dll.set(Node(1))
        self.assertEqual(str(dll.tail), '(1)')
        self.assertEqual(str(dll), '(1)->')
        dll.set(Node(2))
        self.assertEqual(str(dll.tail), '(1)')
        self.assertEqual(str(dll), '(2)->(1)->')
        dll.set(Node(3))
        self.assertEqual(str(dll.tail), '(1)')
        self.assertEqual(str(dll), '(3)->(2)->(1)->')

    def test_remove_last_node(self):
        dll = DoubleLinkedList()
        dll.set(Node(1))
        dll.set(Node(2))
        dll.set(Node(3))
        dll.remove_last()
        self.assertEqual(str(dll), '(3)->(2)->')
        self.assertEqual(str(dll.tail), '(2)')

    def test_move_top(self):
        dll = DoubleLinkedList()
        first_node = Node(1)
        dll.set(first_node)
        dll.set(Node(2))
        dll.set(Node(3))
        self.assertEqual(str(dll), '(3)->(2)->(1)->')
        self.assertEqual(str(dll.tail), '(1)')
        dll.move_top(first_node)
        self.assertEqual(str(dll), '(1)->(3)->(2)->')
        self.assertEqual(str(dll.tail), '(2)')

    def test_multiple_methods(self):
        dll = DoubleLinkedList()
        first_node = Node(1)
        dll.set(first_node)
        dll.set(Node(2))
        dll.set(Node(3))
        self.assertEqual(str(dll), '(3)->(2)->(1)->')
        dll.move_top(first_node)
        self.assertEqual(str(dll), '(1)->(3)->(2)->')
        dll.remove_last()
        self.assertEqual(str(dll), '(1)->(3)->')
        dll.set(Node(4))
        fifth_node = Node(5)
        dll.set(fifth_node)
        self.assertEqual(str(dll), '(5)->(4)->(1)->(3)->')
        dll.set(Node(3))
        self.assertEqual(str(dll), '(3)->(5)->(4)->(1)->(3)->')
        dll.move_top(fifth_node)
        self.assertEqual(str(dll), '(5)->(3)->(4)->(1)->(3)->')


if __name__ == '__main__':
    unittest.main()
