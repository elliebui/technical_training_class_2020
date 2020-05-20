class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color

    def __repr__(self):
        print_color = 'R' if self.color == 'red' else 'B'
        return '%d%s' % (self.value, print_color)


def grandparent(node):
    if not node.parent:
        return None
    return node.parent.parent


# Helper for finding the node's parent's sibling
def pibling(node):
    p = node.parent
    gp = grandparent(node)
    if not gp:
        return None
    if p == gp.left:
        return gp.right
    if p == gp.right:
        return gp.left


class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, None, 'red')

    def __iter__(self):
        yield from self.root.__iter__()

    def insert(self, new_val):
        new_node = self.insert_helper(self.root, new_val)
        self.rebalance(new_node)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                return self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val, current, 'red')
                return current.right
        else:
            if current.left:
                return self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val, current, 'red')
                return current.left

    def rebalance(self, node):
        # case 1: insert the root node. not enforcing rule must be black -> ignore
        if not node.parent:
            return

        # case 2: insert a node below a black node. new node will be red
        # this red node replaces a null black node & this node will
        # have new black child node -> total black nodes for any path
        # from root will remain unchanged
        if node.parent.color == 'black':
            return

        # case 3: the parent and its sibling of the newly inserted node are both red
        # we need to flip color of parent and its sibling to black, grandparent to red
        # -> need to repeat rebalance for grandparent node
        if pibling(node) and pibling(node).color == 'red':
            pibling(node).color = 'black'
            node.parent.color = 'black'
            grandparent(node).color = 'red'
            return self.rebalance(grandparent(node))

        # case 4: newly inserted node has a red parent, but that parent has a black sibling
        # & newly inserted node is on the inside of subtree
        gp = grandparent(node)
        # if there is no grandparent, cases 4 and 5 won't apply
        if not gp:
            return
        # if new node is right of its parent, and parent is left of gradparent
        if gp.left and node == gp.left.right:
            self.rotate_left(node.parent)
            node = node.left
        # if new node is left of its parent, and parent is right of gradparent
        elif gp.right and node == gp.right.left:
            self.rotate_right(node.parent)
            node = node.right
        # after rotation, it then will be case 5

        # case 5: after case 4 or we have an outside subtree already
        # we need to rotate again
        p = node.parent
        gp = p.parent
        # If our new node is a left child of a left child, we rotate right
        if node == p.left:
            self.rotate_right(gp)
        # If our new node is a right of a right, we rotate left
        else:
            self.rotate_left(gp)
        p.color = 'black'
        gp.color = 'red'

    def rotate_left(self, node):
        # Save off the parent of the sub-tree we're rotating)
        p = node.parent

        node_moving_up = node.right
        # After 'node' moves up, the right child will now be a left child
        node.right = node_moving_up.left

        # 'node' moves down, to being a left child
        node_moving_up.left = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        # attach the original node's parent to become node_moving_up parent
        if p:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        # 'node' may have been the root
        # if so, p will be None; 'node' will become the root
        node_moving_up.parent = p

    def rotate_right(self, node):
        p = node.parent
        node_moving_up = node.left
        node.left = node_moving_up.right
        node_moving_up.right = node
        node.parent = node_moving_up
        if p:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p

    def search(self, find_val):
        pass


def print_tree(node, level=0):
    print('   ' * (level - 1) + '+--' * (level > 0) + '%s' % node)
    if node.left:
        print_tree(node.left, level + 1)
    if node.right:
        print_tree(node.right, level + 1)


tree = RedBlackTree(9)
tree.insert(6)
tree.insert(19)


tree.insert(13)

tree.insert(16)
print_tree(tree.root)