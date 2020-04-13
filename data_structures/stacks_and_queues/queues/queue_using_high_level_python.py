class Queue:
    def __init__(self):
        self.arr = []
        # self.next_index = 0
        # self.front_index = -1  # When queue is empty
        # self.queue_size = 0

    def size(self):
        return len(self.arr)

    def enqueue(self, item):
        self.arr.append(item)

    def dequeue(self):
        return self.arr.pop(0)


# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")