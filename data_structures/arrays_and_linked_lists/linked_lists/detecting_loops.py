from data_structures.arrays_and_linked_lists.linked_lists.model.linked_list import LinkedList


def iscircular(linked_list):
    """
    Determine wether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """

    if linked_list.head is None:
        return False

    slow_p = linked_list.head
    fast_p = linked_list.head

    while slow_p and fast_p and fast_p.next:
        slow_p = slow_p.next
        fast_p = fast_p.next.next

        if slow_p == fast_p:
            return True

    return False


# Create a linked list with loop
list_with_loop = LinkedList()
list_with_loop.append(2)
list_with_loop.append(-1)
list_with_loop.append(3)
list_with_loop.append(0)
list_with_loop.append(5)

# Creating a loop where the last node points back to the second node

loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next:
    node = node.next
node.next = loop_start

# Create a linked list without loop
linked_list = LinkedList()
linked_list.append(2)
linked_list.append(-1)
linked_list.append(3)
linked_list.append(0)
linked_list.append(5)

# Create a linked list with one node
linked_list_2 = LinkedList()
linked_list_2.append(2)


print("Pass" if (iscircular(list_with_loop) is True) else "Fail")
print("Pass" if (iscircular(linked_list) is False) else "Fail")
print("Pass" if (iscircular(linked_list_2) is False) else "Fail")