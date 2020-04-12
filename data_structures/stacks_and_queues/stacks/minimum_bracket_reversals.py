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


def minimum_bracket_reversals(input_string):
    """
    Calculate the number of reversals to fix the brackets

    Args:
       input_string(string): Strings to be used for bracket reversal calculation
    Returns:
       int: Number of breacket reversals needed
    """

    # Length of input_string must be even for the brackets to be balanced
    if len(input_string) % 2 != 0:
        return -1

    stack = Stack()

    # This loop will remove all balanced brackets ({})
    # Stack will have brackets like: }}}...{{{
    for bracket in input_string:
        if stack.top() == "{" and bracket == "}":
            stack.pop()
        else:
            stack.push(bracket)

    # Counting number of open brackets
    stack_size = stack.size()
    open_bracket_count = 0
    while not stack.is_empty():
        c = stack.pop()
        if c == "{":
            open_bracket_count += 1
    return stack_size // 2 + open_bracket_count % 2


def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)

    print("output:", output)
    if output == expected_output:
        print("Pass")
    else:
        print("Fail")


test_case_1 = ["}}}}", 2]
test_function(test_case_1)
print("\n")

test_case_2 = ["}}{{", 2]
test_function(test_case_2)
print("\n")

test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
test_function(test_case_3)
print("\n")

test_case_4 = ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
test_function(test_case_4)
print("\n")

test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]
test_function(test_case_5)


test_case_6 = ["{}}}", 1]
test_function(test_case_6)
print("\n")
