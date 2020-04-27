class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_tree_preorder(node):
    if not node:
        return
    print(node.value)
    print_tree_preorder(node.left)
    print_tree_preorder(node.right)


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

    def search(self, find_val):
        return self._search(self.root, find_val)

    def _search(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self._search(current.right, find_val)
            else:
                return self._search(current.left, find_val)
        return False

    def delete(self, del_val):
        return self._delete(self.root, del_val)

    def _delete(self, current, del_val):
        if current is None:
            return current
        elif current.value > del_val:
            current.left = self._delete(current.left, del_val)
        elif current.value < del_val:
            current.right = self._delete(current.right, del_val)
        else:
            # When current.value = del_value, we find the node to be deleted
            # Case 1: node to be deleted doesn't have any child
            if current.left is None and current.right is None:
                current = None
            # Case 2.1: node to be deleted has 1 (right) child
            elif current.left is None and current.right is not None:
                # Make the right child the current node
                current = current.right
            # Case 2.2: node to be deleted has 1 (left) child
            elif current.left is not None and current.right is None:
                # Make the left child the current node
                current = current.left
            # Case 3: node to be deleted has 2 children
            else:
                temp = self.find_min(current.right)
                current.value = temp.value
                current.right = self._delete(current.right, temp.value)
            return current

    def find_min(self, current):
        # loop down to find the lefmost leaf
        while current.left is not None:
            current = current.left
        return current


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(7)

#       4
#      /  \
#     2    5
#    /  \   \
#   1   3    7

# Check search
print ("Pass" if tree.search(4) else "Fail")
print ("Pass" if not tree.search(6) else "Fail")

# Delete elements
tree.delete(4)
tree.delete(2)


#       5
#      / \
#     3   7
#    /
#   1


print_tree_preorder(tree.root)
print ("Pass" if not tree.search(4) else "Fail")
print ("Pass" if not tree.search(2) else "Fail")
