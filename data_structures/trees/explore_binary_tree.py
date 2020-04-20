class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        return self.preorder_print(self.root, "")[:-1]

    def preorder_search(self, root, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        if root:
            if root.value == find_val:
                return True
            elif self.preorder_search(root.left, find_val):
                return True
            elif self.preorder_search(root.right, find_val):
                return True
        return False

    def preorder_print(self, root, tree_nodes):
        """Helper method - use this to create a
        recursive print solution."""
        if root:
            tree_nodes += (str(root.value) + "-")
            tree_nodes = self.preorder_print(root.left, tree_nodes)
            tree_nodes = self.preorder_print(root.right, tree_nodes)
        return tree_nodes


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
print ("Pass" if tree.search(4) else "Fail")
print ("Pass" if not tree.search(6) else "Fail")
print ("Pass" if (tree.print_tree() == '1-2-4-5-3') else "Fail")
