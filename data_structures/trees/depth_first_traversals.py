
# The following code creates implements a simple Tree class and
# creates a tree called my_tree with the following stucture:
#
#     A
#    / \
#   B   C
#  / \
# D   E
#      \
#       F


class Tree:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return str(self.value)


f = Tree("F")
e = Tree("E", None, f)

d = Tree("D")
b = Tree("B", d, e)

c = Tree("C")
a = Tree("A", b, c)

my_tree = a


def print_tree_preorder(tree):
    if not tree:
        return
    print(tree.value)
    print_tree_preorder(tree.left)
    print_tree_preorder(tree.right)


print("Pre-order traversal: ")
print_tree_preorder(my_tree)

"""
Answer:
Pre-order traversal: 
A
B
D
E
F
C
"""


def print_tree_inorder(tree):
    """
    Implement a in-order traversal here

    Args:
       tree(object): A binary tree input
    Returns:
       None
    """
    if not tree:
        return
    print_tree_inorder(tree.left)
    print(tree.value)
    print_tree_inorder(tree.right)


print("In-order traversal: ")
print_tree_inorder(my_tree)

"""
Answer:
In-order traversal: 
D
B
E
F
A
C
"""


def print_tree_postorder(tree):
    """
    Implement a post-order traversal here

    Args:
       tree(object): A binary tree input
    Returns:
       None
    """

    if not tree:
        return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.value)


print("Post-order traversal: ")
print_tree_postorder(my_tree)

"""
Answer:
Post-order traversal: 
D
B
E
F
A
C
"""
