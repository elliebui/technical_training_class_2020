from data_structures.arrays_and_linked_lists.linked_lists.model.linked_list import LinkedList


def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    new_linked_list = LinkedList()
    node = linked_list.head
    while node.next:
        new_linked_list.prepend(node)
        node = node.next

    new_linked_list.prepend(node)
    # new_linked_list.head = node
    return new_linked_list


llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

# print ("Pass" if (llist == reverse(llist)) else "Fail")
print(llist)
print(reverse(llist))
