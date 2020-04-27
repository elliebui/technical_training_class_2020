# Write a function to determine whether or not the input tree is a binary search tree.
#     5
#    / \
#   2   6
#  / \
# 1   3
#      \
#       4
# Assumptions:
#
# Values bound by 0 < n < 100


def _preorder_tree(current, elements=[]):
    if not current:
        return None
    else:
        elements.append(current.value)
        _preorder_tree(current.left, elements)
        _preorder_tree(current.right, elements)
    return elements


INT_MAX = 4294967296
INT_MIN = -4294967296


def check_bst(current):
    """
    Determine whether the input is a binary tree or not

    Args:
       tree(object): A BST object
    Returns:
       bool: True if it is a BST and False if not
    """
    return is_bst(current, INT_MIN, INT_MAX)


def is_bst(current, min_value, max_value):
    # An empty tree is BST
    if current is None:
        return True

    # False if this node violates min/max constraint
    if current.value < min_value or current.value > max_value:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (is_bst(current.left, min_value, current.value - 1) and
            is_bst(current.right, current.value + 1, max_value))


class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return str(self.value)


#     5
#    / \
#   2   6
#  / \
# 1   3
#      \
#       4


f = Node(4)
e = Node(3, None, f)

d = Node(1)
b = Node(2, d, e)

c = Node(6)
a = Node(5, b, c)

my_tree_1 = a
print(check_bst(my_tree_1))
# Shoud be True


#     5
#    / \
#   2   6
#  / \
# 1   3
#      \
#       7

_f = Node(7)
_e = Node(3, None, _f)

_d = Node(1)
_b = Node(2, _d, _e)

_c = Node(6)
_a = Node(5, _b, _c)

my_tree_2= _a
print(check_bst(my_tree_2))
# Should be False

