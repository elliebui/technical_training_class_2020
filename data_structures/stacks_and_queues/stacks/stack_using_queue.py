class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def front(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


class Stack:
    def __init__(self):
        self.queue = Queue()

    def push(self, data):
        self.queue.enqueue(data)

    def pop(self):
        if self.queue.size() == 0:
            return None

        temp_queue = Queue()

        # Put all nodes except for last node from original queue to temp_queue in the same order
        while self.queue.size() != 1:
            temp_queue.enqueue(self.queue.dequeue())

        # Assign last node from original queue to local variable
        last_node = self.queue.dequeue()

        # Put all nodes back to original queue
        while not temp_queue.is_empty():
            self.queue.enqueue(temp_queue.dequeue())

        return last_node

    def top(self):
        """This method should return the first element in queue"""
        if self.queue.size() == 0:
            return None

        temp_queue = Queue()

        # Put all nodes except from original queue to temp_queue in the same order
        while not self.queue.is_empty():
            temp_queue.enqueue(self.queue.dequeue())

        # Dequeue from temp_queue to get the first node and assign to local variable
        first_node = temp_queue.dequeue()

        # Put first node back to original queue
        self.queue.enqueue(first_node)

        # Put the rest of the nodes back to original queue
        while not temp_queue.is_empty():
            self.queue.enqueue(temp_queue.dequeue())

        return first_node

    def size(self):
        return self.queue.size()

    def is_empty(self):
        return self.queue.is_empty()


# Setup
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Test size
print ("Pass" if (stack.size() == 5) else "Fail")

# Test pop
print ("Pass" if (stack.pop() == 50) else "Fail")

# Test push
stack.push(60)
print ("Pass" if (stack.pop() == 60) else "Fail")
print ("Pass" if (stack.pop() == 40) else "Fail")
print ("Pass" if (stack.pop() == 30) else "Fail")
stack.push(50)
print ("Pass" if (stack.size() == 3) else "Fail")