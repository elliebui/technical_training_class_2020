# Write a function to find the height of this binary tree!
#     A
#    / \
#   B   C
#  / \
# D   E
#      \
#       F


def find_height(tree):
    """
    Find the height of a binary tree

    Args:
       tree(object): Input binary tree
    Returns:
       int: The height of the tree
    """
    if not tree:
        return 0

    max_left = find_height(tree.left)
    max_right = find_height(tree.right)

    return max(max_left, max_right) + 1


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

# print(find_height(my_tree))
print("Pass" if (4 == find_height(my_tree)) else "Fail")