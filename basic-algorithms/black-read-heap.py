import unittest

def get_braces(node):
    if node.color == 'red':
        return ('[', ']')
    return ('(', ')')

def draw(string, node, prefix):
    if not node:
         return prefix + ' x'+'\n'
    # left, right = get_braces(node)
    # new_string = prefix+' ' + left + str(node.value) + right + '\n'
    color_letter = ''
    if node.color == 'red':
        color_letter = 'R'
    else:
        color_letter = 'B'
    new_string = prefix+' ' + str(node.value) + color_letter + '\n'
    new_string += draw(string, node.left, prefix + '--')
    new_string += draw(string, node.right, prefix + '--')
    return new_string

class Node:
    def __init__(self, value, color = 'red'):
        self.parent = None
        self.left = None
        self.right = None
        self.color = color
        self.value = value

    def __str__(self):
        return draw('', self, '')

    def set_left(self, node):
        node.parent = self
        self.left = node

    def set_right(self, node):
        node.parent = self
        self.right = node

    def has_parent(self):
        return self.parent is not None
    
    def has_grandparent(self):
        if not self.has_parent():
            return False
        return self.parent.parent is not None

    def get_parent(self):
        return self.parent
    
    def get_grandparent(self):
        if self.has_parent():
            return self.parent.parent
    
    def get_parent_sibling(self):
        parent = self.get_parent()
        if not self.has_parent() or not self.has_grandparent():
            raise Exception('Has no parent or no grandparent')
        grandparent = self.get_grandparent()
        if parent is grandparent.left:
            return grandparent.right
        else:
            return grandparent.left
    
    def is_left(self):
        parent = self.get_parent()
        if not self.has_parent():
            raise Exception('Has no parent')
        return parent.left is self

    def is_right(self):
        parent = self.get_parent()
        if not self.has_parent():
            raise Exception('Has no parent')
        return parent.right is self

    def is_inside(self):
        if not self.has_parent():
            raise Exception('Has no parent')
        parent = self.get_parent()
        if self.is_left() and parent.is_right():
            return True
        if self.is_right() and parent.is_left():
            return True
        return False

def rotate_left(node):
    parent = node.get_parent()
    grandparent = node.get_grandparent()
    grandparent.set_left(node)
    parent.left = None
    parent.right = None
    node.set_left(parent)

def rotate_right(node):
    parent = node.get_parent()
    grandparent = node.get_grandparent()
    grandgrandparent = grandparent.get_parent()
    if grandparent.is_right():
        grandgrandparent.set_right(parent)
        parent.set_right(grandparent)
    else:
        raise Exception('No implemented for grandparents being left')


"""
    inserting
    if less than current node add to the left
    otherwise to the right
    and set as a red node
    then rebalance
    consider 5 cases
    1. if it is a root do nothing
    2. if the parent node is black also do not do anything
    3. if the parent and the sibling of the newly inserted node are red
"""



class BlackRedTreeTests(unittest.TestCase):

    def test_is_inside_0(self):
        root = Node(9)
        root.set_left(Node(6))
        root.set_right(Node(19))
        root.right.set_left(Node(13))
        root.right.left.set_right(Node(16))
        self.assertTrue(root.right.left.right.is_inside())

    def test_is_inside_1(self):
        root = Node(9)
        root.set_left(Node(6))
        root.set_right(Node(19))
        root.right.set_left(Node(16))
        root.right.left.set_left(Node(13))
        self.assertFalse(root.right.left.left.is_inside())

    def test_rotate_left_0(self):
        root = Node(9)
        root.set_left(Node(6))
        root.set_right(Node(19))
        root.right.set_left(Node(13))
        last_node = Node(16)
        root.right.left.set_right(last_node)
        print(root)
        rotate_left(last_node)
        print(root)


    def test_rotate_right_0(self):
        root = Node(9)
        root.set_left(Node(6))
        root.set_right(Node(19))
        root.right.set_left(Node(16))
        last_node = Node(13)
        root.right.left.set_left(last_node)
        rotate_right(last_node)
        # print(last_node)

    def test_binary_tree_drawing(self):
        root = Node(9)
        root.set_left(Node(6))
        root.set_right(Node(19))
        root.right.set_left(Node(13))
        last_node = Node(16)
        root.right.left.set_right(last_node)

        expected_str = """ 9R
-- 6R
---- x
---- x
-- 19R
---- 13R
------ x
------ 16R
-------- x
-------- x
---- x
"""
        actual_str = str(root)
        self.assertEqual(expected_str, actual_str)

if __name__ == '__main__':
    unittest.main()
