class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def to_list(self):
        # Function to turn Linked List into Python List
        python_list = []
        if self.head is None:
            return None

        node = self.head
        while node:
            python_list.append(node.data)
            node = node.next

        return python_list


def reverse_stack(stack):
    """
    Reverse a given input stack

    Args:
       stack(stack): Input stack to be reversed
    Returns:
       stack: Reversed Stack
    """

    if stack.is_empty():
        return None

    previous = None
    current = stack.head

    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next

    stack.head = previous


def test_function(test_case):
    stack = Stack()
    for num in test_case:
        stack.push(num)

    reverse_stack(stack)
    index = 0
    while not stack.is_empty():
        popped = stack.pop()
        if popped != test_case[index]:
            print("Fail")
            return
        else:
            index += 1
    print("Pass")


test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)

test_case_2 = [1]
test_function(test_case_2)


# This following method returns the reversed stack as a new stack
# def reverse_stack(stack):

# new_stack = Stack()
#
# if stack.is_empty():
#     return None
#
# current = stack.head
# while current:
#     new_stack.push(current.data)
#     print(current.data)
#     current = current.next
#
# print("output:", new_stack.to_list())
# return new_stack