# Find the lowest common ancestor of two nodes in the tree.
#
# Lowest common ancestor is the loweest node in which the two provided nodes are decendents. For example in the tree below the selected nodes of 1 and 6 give us a lowest common ancestor of 5 as its the lowest amount in which both nodes are decendents.
#
# Given the following binary tree:
#
#     5
#    / \
#   2   6
#  / \
# 1   3
#      \
#       4


def lowest_common_ancestor(current, n1, n2):
    """
    Determine the lowest common ancestor

    Args:
       tree(object): A BST object
    Returns:
       int: Lowest shared ancestor
    """
    if current is None:
        return None

    # If current node is larger than both input nodes
    # Both input nodes are in the left subtree
    if current.value > n1 and current.value > n2:
        return lowest_common_ancestor(current.left, n1, n2)

    # If current node is smaller than both input nodes
    # Both input nodes are in the right subtree
    if current.value < n1 and current.value < n2:
        return lowest_common_ancestor(current.right, n1, n2)

    return current.value


class Tree:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return str(self.value)


def print_tree_preorder(tree):
    if not tree:
        return
    print(tree.value)
    print_tree_preorder(tree.left)
    print_tree_preorder(tree.right)


f = Tree(4)
e = Tree(3, None, f)

d = Tree(1)
b = Tree(2, d, e)

c = Tree(6)
a = Tree(5, b, c)

my_tree = a

print("Pass" if 2 == lowest_common_ancestor(my_tree, 1, 4) else "Fail")
print("Pre-order traversal: ")
print_tree_preorder(my_tree)
