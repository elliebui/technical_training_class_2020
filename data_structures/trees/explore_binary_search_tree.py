class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_tree_inorder(tree):
    """
    Implement a in-order traversal here

    Args:
       tree(object): A binary tree input
    Returns:
       None
    """
    if not tree:
        return None
    print_tree_inorder(tree.left)
    print(tree.value)
    print_tree_inorder(tree.right)


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self._insert(self.root, new_val)

    def _insert(self, current, new_val):
        if current.value <= new_val:
            if not current.right:
                # If there's no subtree on the right of current node
                # Create a new node
                current.right = Node(new_val)
            else:
                # If there's a subtree on the right of current node
                # Repeat recursive function
                self._insert(current.right, new_val)
        else:
            if not current.left:
                current.left = Node(new_val)
            else:
                self._insert(current.left, new_val)

    def preorder_print(self):
        return self._preorder_print(self.root, "")[:-1]

    def _preorder_print(self, root, tree_nodes):
        """Helper method - use this to create a
        recursive print solution."""
        if root:
            tree_nodes += (str(root.value) + "-")
            tree_nodes = self._preorder_print(root.left, tree_nodes)
            tree_nodes = self._preorder_print(root.right, tree_nodes)
        return tree_nodes

    def search(self, find_val):
        return self._search(self.root, find_val)

    def _search(self, current, find_val):
        if current is None:
            return False

        if current.value == find_val:
            return True
        elif current.value < find_val:
            return self._search(current.right, find_val)
        else:
            return self._search(current.left, find_val)


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

#       4
#     2    5
#   1   3

print(tree.preorder_print())

# Check search
print(tree.search(4))
print(tree.search(1))
print(tree.search(6))

print("Pass" if tree.search(4) else "Fail")
print("Pass" if tree.search(1) else "Fail")
print("Pass" if not tree.search(6) else "Fail")