class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        self.head = Node(value)
        self.head.next = node

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    value_hash_table = dict()

    curr_node_1 = llist_1.head
    while curr_node_1:
        value_hash_table[curr_node_1.value] = True
        # Time complexity: O(1)
        curr_node_1 = curr_node_1.next
    # Time complexity: O(N)

    curr_node_2 = llist_2.head
    while curr_node_2:
        value_hash_table[curr_node_2.value] = True
        # Time complexity: O(1)
        curr_node_2 = curr_node_2.next
    # Time complexity: O(N)

    union_llist = LinkedList()
    for value in value_hash_table:
        union_llist.prepend(value)
        # Time complexity: O(1)
    # Time complexity: O(N)

    if union_llist.size() != 0:  # Time complexity: O(N)
        return union_llist
    # Total time complexity: O(N)


def intersection(llist_1, llist_2):
    value_hash_table = dict()
    intersection_hash_table = dict()
    intersection_llist = LinkedList()

    curr_node_1 = llist_1.head
    while curr_node_1:
        if curr_node_1.value not in value_hash_table:
            value_hash_table[curr_node_1.value] = True
        # Time complexity: O(1)
        curr_node_1 = curr_node_1.next
    # Time complexity: O(N)

    curr_node_2 = llist_2.head
    while curr_node_2:
        if curr_node_2.value in value_hash_table and curr_node_2.value not in intersection_hash_table:
            intersection_llist.prepend(curr_node_2.value)
            intersection_hash_table[curr_node_2.value] = True
            # Time complexity: O(1)
        curr_node_2 = curr_node_2.next
    # Time complexity: O(N)

    if intersection_llist.size() != 0:  # Time complexity: O(N)
        return intersection_llist
    # Total time complexity: O(N)


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.prepend(i)

for i in element_2:
    linked_list_2.prepend(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.prepend(i)

for i in element_2:
    linked_list_4.prepend(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

"""
Answer:
32 -> 9 -> 11 -> 1 -> 2 -> 35 -> 65 -> 6 -> 4 -> 3 -> 21 -> 
4 -> 6 -> 21 -> 
7 -> 8 -> 9 -> 11 -> 21 -> 1 -> 2 -> 35 -> 65 -> 6 -> 4 -> 3 -> 23 -> 
None
"""