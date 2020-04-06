from data_structures.arrays_and_linked_lists.linked_lists.model.node import Node


class SortedLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Append a value to the Linked List in ascending sorted order

        Args:
           value(int): Value to add to Linked List
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        # If value is smaller than the head of ordered list
        # prepend it to the beginning of list
        if value < self.head.value:
            tmp = self.head
            self.head = new_node
            self.head.next = tmp
            return

        node = self.head

        # If value is in between values of nodes in the ordered list
        # add it in between the nodes
        while node.next:
            if node.value <= value <= node.next.value:
                tmp = node.next
                node.next = new_node
                new_node.next = tmp
                return

            node = node.next

        # If value is greater than the last Node's value in the ordered list
        # append it to the end of list
        node.next = new_node



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


def sort(array):
    """
    Given an array of integers, use SortedLinkedList to sort them and return a sorted array.

    Args:
       array(array): Array of integers to be sorted
    Returns:
       array: Return sorted array
    """
    sorted_array = SortedLinkedList()
    for integer in array:
        sorted_array.append(integer)

    return sorted_array.to_list()

# Test cases
linked_list = SortedLinkedList()
linked_list.append(3)
print ("Pass" if (linked_list.head.value == 3) else "Fail")

linked_list.append(2)
print ("Pass" if (linked_list.head.value == 2) else "Fail")

linked_list.append(4)
node = linked_list.head.next.next
print ("Pass" if (node.value == 4) else "Fail")


# Test case
print ("Pass" if (sort([4, 8, 2, 1, -3, 1, 5]) == [-3, 1, 1, 2, 4, 5, 8]) else "Fail")
