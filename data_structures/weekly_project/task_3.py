import sys
from queue import PriorityQueue
from collections import defaultdict


class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def get_frequency(string):
    frequency_map = defaultdict(int)
    for char in string:
        frequency_map[char] += 1

    return frequency_map
    # Time complexity: O(N)


def build_min_heap(string):
    min_heap = PriorityQueue()
    frequency_map = get_frequency(string)
    for char, freq in frequency_map.items():  # Time complexity: O(N)
        min_heap.put(HeapNode(char, freq))  # Time complexity: O(logN)
        # (put a node at the end and swap nodes to maintain min heap; worst case swap logN times - height of min heap)
    # Time complexity: O(NlogN)

    while min_heap.qsize() > 1:  # Time complexity: O(1)
        left_child = min_heap.get()  # Time complexity: O(logN)
        # (get node at the top and swap nodes to maintain min heap; worst case swap logN times - height of min heap)
        right_child = min_heap.get()  # Time complexity: O(logN)
        new_node = HeapNode("*", left_child.freq + right_child.freq)
        new_node.left = left_child
        new_node.right = right_child
        min_heap.put(new_node)  # Time complexity: O(logN)
    # Time complexity: O(NlogN)

    return min_heap
    # Time complexity: O(NlogN)


def build_string_to_code_map(string):
    string_to_code_map = dict()
    code = ""

    min_heap = build_min_heap(string)  # Time complexity: O(NlogN)
    huffman_tree = min_heap.get()  # Time complexity: O(1) (min heap only has 1 node here)

    def _get_string_to_code_map(node, code):
        if not node:
            return
        if node.left is None and node.right is None:
            string_to_code_map[node.char] = code
            code = ""
        _get_string_to_code_map(node.left, code + "0")
        _get_string_to_code_map(node.right, code + "1")

    _get_string_to_code_map(huffman_tree, code)  # Time complexity: N (traverse N nodes)

    return string_to_code_map, huffman_tree
    # Time complexity: O(NlogN)


def huffman_encoding(string):
    string_to_code_map, huffman_tree = build_string_to_code_map(string)  # Time complexity: O(NlogN)
    encoded_string = ""
    for char in string:  # Time complexity: O(N)
        encoded_string += string_to_code_map[char]

    return encoded_string, huffman_tree


def huffman_decoding(string, tree):
    decoded_string = ""
    current = tree
    for char in string:  # Time complexity: O(N)
        if char == "0":
            current = current.left
        else:
            current = current.right

        if current.left is None and current.right is None:
            decoded_string += current.char
            current = tree

    return decoded_string
    # Time complexity: O(N)


# Total time complexity: O(NlogN)
if __name__ == "__main__":
    codes = {}
    a_great_sentence = "The bird is the word"
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

"""
Answer:
The size of the data is: 69

The content of the data is: The bird is the word

The size of the encoded data is: 36

The content of the encoded data is: 1000111111100100001101110000101110110110100011111111001101010011100001

The size of the decoded data is: 69

The content of the encoded data is: The bird is the word
"""
