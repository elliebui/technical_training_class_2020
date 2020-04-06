from data_structures.arrays_and_linked_lists.linked_lists.model.node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        self.head = Node(value)
        self.head.next = node

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])
