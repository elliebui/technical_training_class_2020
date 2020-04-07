from data_structures.arrays_and_linked_lists.linked_lists.model.linked_list import LinkedList


def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    if linked_list.head is None:
        return None

    previous = None
    current = linked_list.head

    while current:
        next = current.next
        current.next = previous

        previous = current
        current = next

    linked_list.head = previous
    return linked_list


llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

print(llist)
print(reverse(llist))
