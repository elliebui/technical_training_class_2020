# Write a function to count the leafs on this binary tree.
#
#     A
#    / \
#   B   C
#  / \
# D   E
#      \
#       F


def count_leafs(tree):
    """
    Find the number of leafs on a binary tree

    Args:
       tree(object): Input binary tree
    Returns:
       int: The number of leafs of the tree
    """
    if not tree:
        return 0
    if not tree.left and not tree.right:
        return 1


    left_count = count_leafs(tree.left)
    right_count = count_leafs(tree.right)
    print(left_count + right_count)

    return left_count + right_count


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

print("Pass" if (3 == count_leafs(my_tree)) else "Fail")