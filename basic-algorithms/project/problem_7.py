import unittest

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:

    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, path_as_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        # path_section = path_as_list[0]
        current_node = self.root
        last_index = len(path_as_list) - 1
        for i, section in enumerate(path_as_list):
            if section not in current_node.children:
                handler_to_set = None
                if i == last_index:
                    handler_to_set = handler
                current_node.insert(section, handler_to_set)
            else:
                if i == last_index:
                    current_node.children[section].handler = handler
                    return
            current_node = current_node.children[section]

    def find(self, path_as_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        last_index = len(path_as_list) - 1
        for i, section in enumerate(path_as_list):
            if section not in current_node.children:
                return None
            if i == last_index and current_node.children[section]:
                return current_node.children[section]
            current_node = current_node.children[section]


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, section, handler = None):
        new_node = RouteTrieNode(handler)
        self.children[section] = new_node


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler = None, not_found_handler = None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root_hander = root_handler
        self.not_found_handler = not_found_handler
        self.route_trie = RouteTrie()

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_as_list = self._split_path(path)
        self.route_trie.insert(path_as_list, handler)

    def lookup(self, path):
        if not path or path == '':
            raise Exception('path is empty or None')
        if path == '/':
            return self.root_hander
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_as_list = self._split_path(path)
        node = self.route_trie.find(path_as_list)
        if not node or not node.handler:
            return self.not_found_handler
        return node.handler

    def _split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return [x for x in path.split('/') if x.strip()]


class Tests(unittest.TestCase):

    def test_0(self):
        router = Router()
        self.assertListEqual(['home'], router._split_path('/home'))
        self.assertListEqual(['home', 'about'], router._split_path('/home/about'))
        self.assertListEqual(['home', 'about'], router._split_path('/home/about/'))
        self.assertListEqual(['home', 'about', 'me'], router._split_path('/home/about/me'))

    def test_1(self):
        router = Router("root handler", "not found handler")
        router.add_handler("/home/about", "about handler")
        self.assertEqual(router.lookup("/"), 'root handler')
        self.assertEqual(router.lookup("/home"), 'not found handler')
        self.assertEqual(router.lookup("/home/about"), 'about handler')
        self.assertEqual(router.lookup("/home/about/"), 'about handler')
        self.assertEqual(router.lookup("/home/about/me"), 'not found handler')
        self.assertEqual(router.lookup("/home/about/me/"), 'not found handler')

    def test_2(self):
        router = Router("Welcome!", "404 Oups!")
        router.add_handler("/home/team/hr/senior/Wolfgang", "Our head of HR")
        router.add_handler("/home/team/hr/", "HR")
        router.add_handler('/home', 'All you wish!')
        router.add_handler("/home/team/hr/senior/Wolfgang/family_tree", "He is our founder, so more stuff about him.")
        self.assertEqual(router.lookup("/"), 'Welcome!')
        self.assertEqual(router.lookup("/home/team"), '404 Oups!')
        self.assertEqual(router.lookup("/home/team/"), '404 Oups!')
        self.assertEqual(router.lookup("/home/team/hr"), 'HR')
        self.assertEqual(router.lookup("/home/team/hr/senior/Wolfgang/"), 'Our head of HR')
        self.assertEqual(router.lookup("/home/"), 'All you wish!')
        self.assertEqual(router.lookup("/home/team/hr/senior/Wolfgang/family_tree"), "He is our founder, so more stuff about him.")


if __name__ == '__main__':
    unittest.main()
