from collections import defaultdict


# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)

    def insert(self, char):
        return self.children[char]

    def suffixes(self, suffix=''):
        suffix_list = []

        if self.is_word and suffix:
            suffix_list.append(suffix)

        for char, trie_node in self.children.items():
            suffix_list.extend(trie_node.suffixes(suffix + char))

        return suffix_list
        # This will take O(M*N), where M is number of children of node and
        # N is number of nodes below the prefix node


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_list = list()

    def insert(self, word):
        node = self.root

        for char in word:
            node = node.insert(char)

        node.is_word = True

    def find(self, prefix):
        node = self.root

        for char in prefix:
            node = node.children[char]

        return node
    #   This will take O(N) time (number of characters in prefix * constant lookup time of each char)

    def autocomplete(self, prefix):
        node = self.find(prefix)
        return node.suffixes()


trie = Trie()

words = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

for word in words:
    trie.insert(word)


print(trie.autocomplete("a"))
print(trie.autocomplete("fu"))
print(trie.autocomplete(""))


"""
['nt', 'nthology', 'ntagonist', 'ntonym']
['n', 'nction']
['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']
"""
