from collections import defaultdict


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.handler = None
        self.children = defaultdict(RouteTrieNode)

    def insert(self, part):
        # Insert the node as before
        return self.children[part]


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = None

    def insert(self, path_parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root

        for part in path_parts:
            node = node.insert(part)

        node.handler = handler

    def find(self, path_parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root

        for part in path_parts:
            node = node.children[part]

        return node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_response):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie()
        self.root_handler = root_handler
        self.not_found_response = not_found_response

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_parts = self.split_path(path)
        return self.route_trie.insert(path_parts, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_parts = self.split_path(path)

        # If path ends with trailing slash, remove the empty path part at the end
        if path_parts[-1] == "":
            path_parts = path_parts[:-1]

        # If after removing trailing slash and path_parts is empty list, it is root
        if not path_parts:
            return self.root_handler

        handler = self.route_trie.find(path_parts)
        if handler:
            return handler

        return self.not_found_response

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        return path.split("/")[1:]


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route

router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
# router = Router("root handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one


# Time complexity: O(N) with N is height of the RouteTrie
"""
root handler
not found handler
about handler
about handler
not found handler
"""