import unittest

def fill_suffixes(arr, string, node):
    if node.is_word and string != '':
        arr.append(string)
    if node.children:
        for char in node.children:
            fill_suffixes(arr, string+char, node.children[char])


class TrieNode:
    def __init__(self, is_word=False):
        # Initialize this node in the Trie
        self.is_word = is_word
        self.children = {}

    def insert(self, char, is_last=False):
        new_node = TrieNode(is_last)
        self.children[char] = new_node

    def suffixes(self):
        arr = []
        fill_suffixes(arr, '', self)
        return arr


# The Trie itself containing the root node and insert/find functions


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        if word == '' or word is None:
            raise Exception('Must be a string')

        current_node = self.root
        last_index = len(word) - 1
        for i, char in enumerate(word.lower()):
            if char not in current_node.children:
                is_last = False
                if i == last_index:
                    is_last = True
                current_node.insert(char, is_last)
            current_node = current_node.children[char]

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current_node = self.root
        last_index = len(prefix) - 1
        for i, char in enumerate(prefix.lower()):
            if char not in current_node.children:
                return None
            if i == last_index and current_node.children[char]:
                return current_node.children[char]
            current_node = current_node.children[char]


class Tests(unittest.TestCase):

    def test_empty_trie(self):
        empty_trie = Trie()
        node = empty_trie.find('h')
        self.assertIsNone(node)

    def test_0(self):
        # basic_trie = {
        #     # a and add word
        #     'a': {
        #         'd': {
        #             'd': {'word_end': True},
        #             'word_end': False},
        #         'word_end': True},
        #     # hi word
        #     'h': {
        #         'i': {'word_end': True},
        #         'word_end': False}}
        basic_trie = Trie()
        basic_trie.insert('Add')
        basic_trie.insert('hI')
        node = basic_trie.find('h')
        arr = node.suffixes()
        self.assertListEqual(['i'], arr)
        node = basic_trie.find('a')
        arr = node.suffixes()
        self.assertListEqual(['dd'], arr)

    def test_1(self):
        trie = Trie()
        word_list = [
            "fun", "function", "factory"
        ]
        for word in word_list:
            trie.insert(word)

        f_node = trie.find('f')
        f_suffixes = f_node.suffixes()
        self.assertListEqual(['un', 'unction', 'actory'], f_suffixes)

        fu_node = trie.find('fu')
        fu_suffixes = fu_node.suffixes()
        self.assertListEqual(['n', 'nction'], fu_suffixes)

        fun_node = trie.find('fun')
        fun_suffixes = fun_node.suffixes()
        self.assertListEqual(['ction'], fun_suffixes)

        func_node = trie.find('func')
        func_suffixes = func_node.suffixes()
        self.assertListEqual(['tion'], func_suffixes)

        function_node = trie.find('function')
        function_suffixes = function_node.suffixes()
        self.assertListEqual([], function_suffixes)

    def test_2(self):
        trie = Trie()
        word_list = [
            "ant", "anthology", "antagonist", "antonym"
        ]
        for word in word_list:
            trie.insert(word)

        a_node = trie.find('a')
        a_suffixes = a_node.suffixes()
        self.assertListEqual(
            ['nt', 'nthology', 'ntagonist', 'ntonym'], a_suffixes)

        an_node = trie.find('an')
        an_suffixes = an_node.suffixes()
        self.assertListEqual(
            ['t', 'thology', 'tagonist', 'tonym'], an_suffixes)

        ant_node = trie.find('ant')
        ant_suffixes = ant_node.suffixes()
        self.assertListEqual(
            ['hology', 'agonist', 'onym'], ant_suffixes)

    def test_3(self):
        trie = Trie()
        word_list = ["trie", "trigger", "trigonometry", "tripod"]
        for word in word_list:
            trie.insert(word)

        t_node = trie.find('t')
        t_suffixes = t_node.suffixes()
        self.assertListEqual(
            ["rie", "rigger", "rigonometry", "ripod"], t_suffixes)

    def test_complex(self):
        trie = Trie()
        word_list = ['abject',
                     'aberration',
                     'abjure',
                     'abnegation',
                     'abrogate',
                     'expurgate',
                     'fallacious',
                     'fatuous',
                     'fetter',
                     'flagrant',
                     'foil',
                     'forbearance',
                     'fortuitous',
                     'fractious',
                     'palliate',
                     'panacea',
                     'paradigm',
                     'pariah',
                     'partisan',
                     'paucity',
                     'pejorative',
                     'pellucid',
                     'penchant',
                     'penurious',
                     'pert',
                     'pernicious',
                     'pertinacious',
                     'phlegmatic',
                     'philanthropic',
                     'pithy',
                     'staid',
                     'stolid',
                     'subjugate',
                     'surfeit',
                     'surreptitious',
                     'swarthy',
                     'tangential',
                     'tome',
                     'toady',
                     'torpid',
                     'travesty',
                     'trenchant',
                     'trite',
                     'truculent',
                     'turpitude',
                     'ubiquitous',
                     'umbrage',
                     'wily',
                     'tirade'
                     ]
        for word in word_list:
            trie.insert(word)


        w_node = trie.find('w')
        w_suffixes = w_node.suffixes()
        self.assertListEqual(["ily"], w_suffixes)

        abj_node = trie.find('abj')
        abj_suffixes = abj_node.suffixes()
        self.assertListEqual(["ect", "ure"], abj_suffixes)

if __name__ == '__main__':
    unittest.main()
