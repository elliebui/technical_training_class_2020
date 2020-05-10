import sys
from queue import PriorityQueue


class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def get_frequency(string):
    frequency_map = dict()
    for char in string:
        if char in frequency_map:
            frequency_map[char] += 1
        else:
            frequency_map[char] = 1

    return frequency_map


def build_min_heap(string):
    min_heap = PriorityQueue()
    frequency_map = get_frequency(string)
    for char, freq in frequency_map.items():
        min_heap.put(HeapNode(char, freq))

    while min_heap.qsize() > 1:
        left_child = min_heap.get()
        right_child = min_heap.get()
        new_node = HeapNode("*", left_child.freq + right_child.freq)
        new_node.left = left_child
        new_node.right = right_child
        min_heap.put(new_node)

    return min_heap


def build_string_to_code_map(string):
    string_to_code_map = dict()
    code = ""

    min_heap = build_min_heap(string)
    huffman_tree = min_heap.get()

    def _get_string_to_code_map(node, code):
        if node.left is None and node.right is None:
            string_to_code_map[node.char] = code
            code = ""
        if node.left:
            _get_string_to_code_map(node.left, code + "0")
        if node.right:
            _get_string_to_code_map(node.right, code + "1")

    _get_string_to_code_map(huffman_tree, code)

    return string_to_code_map, huffman_tree


def huffman_encoding(string):
    string_to_code_map, huffman_tree = build_string_to_code_map(string)
    encoded_string = ""
    for char in string:
        encoded_string += string_to_code_map[char]

    return encoded_string, huffman_tree


def huffman_decoding(string, tree):
    decoded_string = ""
    current = tree
    for char in string:
        if char == "0":
            current = current.left
        else:
            current = current.right

        if current.left is None and current.right is None:
            decoded_string += current.char
            current = tree

    return decoded_string


if __name__ == "__main__":
    codes = {}
    a_great_sentence = "The bird is the word"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


"""
Answer:
The size of the data is: 69

The content of the data is: The bird is the word

The size of the encoded data is: 36

The content of the encoded data is: 1000111111100100001101110000101110110110100011111111001101010011100001

The size of the decoded data is: 69

The content of the encoded data is: The bird is the word
"""