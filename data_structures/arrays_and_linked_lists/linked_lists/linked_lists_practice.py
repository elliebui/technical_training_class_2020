from data_structures.arrays_and_linked_lists.linked_lists.model.node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """ Append a value to the end of the list. """
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def to_list(self):
        # Function to turn Linked List into Python List
        python_list = []
        if self.head is None:
            return python_list

        node = self.head
        while node:
            python_list.append(node.value)
            node = node.next

        return python_list

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        self.head = Node(value)
        self.head.next = node

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        if self.head is None:
            raise Exception("List is empty.")

        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
        raise Exception("Value is not found in list.")

    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head is None:
            raise Exception("List is empty.")

        node = self.head

        if node.value == value:
            self.head = self.head.next
            return

        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

        raise Exception("Value is not found in list.")

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head is None:
            raise Exception("List is empty.")

        node = self.head
        self.head = self.head.next
        return node.value

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        node = self.head
        index = 0

        if pos == 0:
            self.prepend(value)
        elif pos >= self.size():
            self.append(value)
        else:
            while node.next:
                index += 1
                if pos == index:
                    tmp = node.next
                    new_node = Node(value)
                    node.next = new_node
                    new_node.next = tmp
                    return
                node = node.next

    def size(self):
        """ Return the size or length of the linked list. """
        size = 0
        if self.head is None:
            return size

        node = self.head
        while node.next:
            size += 1
            node = node.next

        size += 1

        return size


# Test your implementation here

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"