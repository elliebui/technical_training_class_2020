class Queue:
    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1  # When queue is empty
        self.queue_size = 0

    def enqueue(self, value):
        # Assign element to next index in array
        self.arr[self.next_index] = value
        # Increment next_index
        self.next_index = (self.next_index + 1) % len(self.arr)
        # If queue is empty, set front_index to 0
        if self.front_index == -1:
            self.front_index = 0
        # Increment queue size
        self.queue_size += 1

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        if self.is_empty():
            return None

        return self.arr[self.front_index]

    def dequeue(self):
        # If queue is empty, reset pointers to initial values
        if self.is_empty():
            self.next_index = 0
            self.front_index = -1  # When queue is empty
            return None

        # Shift the head over so that it refers to the next index
        front = self.arr[self.front_index]
        # self.arr[self.front_index] = self.arr[self.next_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        # Decrease queue size and return front
        self.queue_size -= 1
        return front

    def _handle_queue_capacity_full(self):
        old_arr = self.arr

        # Create new array with double length of old array
        self.arr = [0 for _ in range(2 * len(old_arr))]

        index = 0

        # Copy old array from front index to end of array
        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1

        # When next_index is in front of front_index, copy from next index to front
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1

        # Reset pointers
        self.front_index = 0
        self.next_index = index

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
