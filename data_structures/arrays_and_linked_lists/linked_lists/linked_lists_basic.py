from data_structures.arrays_and_linked_lists.linked_lists.node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return node.next

    def to_list(self):
        # Function to turn Linked List into Python List
        python_list = []
        if self.head is None:
            return None

        node = self.head
        while node:
            python_list.append(node.value)
            node = node.next

        return python_list


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)

node = linked_list.head
while node:
    print(node.value)
    node = node.next


linked_list.to_list()
print(linked_list.to_list())


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        # Method to append to the tail of the list
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        # Assign new Node to tail.next (new tail)
        self.tail.next = DoubleNode(value)
        # Create connection between the old tail as the previous of the new tail
        self.tail.next.previous = self.tail
        # Assign the new tail as current tail
        self.tail = self.tail.next
        return


linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(-2)
linked_list.append(4)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list.tail
while node:
    print(node.value)
    node = node.previous