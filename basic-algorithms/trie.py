import unittest

class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        """
        Add `word` to trie
        """

        if word == '' or word is None:
            raise Exception('Must be a number')

        if self.exists(word):
            return

        current_node = self.root
        last_index = len(word) - 1
        for i, char in enumerate(word):
            if char not in current_node.children:
                new_node = TrieNode()
                current_node.children[char] = new_node
                if i == last_index:
                    new_node.is_word = True
            current_node = current_node.children[char]
                

    
    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            
            current_node = current_node.children[char]
        
        return current_node.is_word

class TrieTests(unittest.TestCase):

    def test_1(self):
        trie = Trie()
        trie.add('a')
        self.assertTrue(trie.root.children['a'].is_word)

    def test_2(self):
        trie = Trie()
        trie.add('add')
        self.assertFalse(trie.root.children['a'].children['d'].is_word)
        self.assertTrue(trie.root.children['a'].children['d'].children['d'].is_word)

    def test_3(self):
        trie = Trie()
        trie.add('add')
        self.assertTrue(trie.exists('add'))

    def test_4(self):
        trie = Trie()
        self.assertRaises(Exception, trie.add, '')
        self.assertRaises(Exception, trie.add, None)

    def test_5(self):
        trie = Trie()
        trie.add('add')
        trie.add('zoo')
        trie.add('abdominal')
        trie.add('abandon')
        self.assertTrue(trie.exists('add'))
        self.assertTrue(trie.exists('abandon'))
        self.assertTrue(trie.exists('abdominal'))
        self.assertTrue(trie.exists('zoo'))


if __name__ == '__main__':
    unittest.main()