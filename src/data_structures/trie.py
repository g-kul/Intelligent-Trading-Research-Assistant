class TrieNode:
    def __init__(self):
        self._children = {}
        self._is_end_of_word = False


class Trie:
    def __init__(self):
        self._root = TrieNode()

    def insert(self, word):
        node = self._root

        for char in word:
            if char not in node._children:
                node._children[char] = TrieNode()
            node = node._children[char]
        node._is_end_of_word = True

    def search(self, word):
        node = self._root

        for char in word:
            if char not in node._children:
                return False
            node = node._children[char]
        return node._is_end_of_word

    def starts_with(self, prefix):
        node = self._root

        for char in prefix:
            if char not in node._children:
                return False
            node = node._children[char]
        return True
