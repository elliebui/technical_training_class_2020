class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity=5):
        self.head = None
        self.end = None
        self.hash_map = dict()
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.hash_map:
            return -1

        # if key exists in map, then remove node from list
        # and set it as head of list (most recently used)
        node = self.hash_map[key]
        self.remove(node)
        self.size += 1
        self.set_head(node)
        return node.value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key not in self.hash_map:
            new_node = Node(key, value)
            # if cache reaches capacity, remove key from hash_map
            # and remove end node (least recently used)
            if self.size == self.capacity:
                self.hash_map.pop(self.end.key)
                self.remove(self.end)

            # else set the new node as head node (most recently used)
            self.set_head(new_node)
            self.hash_map[key] = new_node
            self.size += 1

        else:
            node = self.hash_map[key]
            node.value = value
            self.remove(node)
            self.set_head(node)

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.end = node.prev
        self.size -= 1

    def set_head(self, node):
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node

        if not self.end:
            self.end = self.head


our_cache = LRUCache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print("get(1):", our_cache.get(1))  # returns 1
print("get(2):", our_cache.get(2))  # returns 2
print("get(9):", our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print("get(3):", our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

"""
Answer:
get(1): 1
get(2): 2
get(9): -1
get(3): -1

"""