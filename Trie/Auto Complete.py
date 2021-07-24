class Trie:
    def __init__(self):
        self.root = {}
        self.end = "*"

    def prepareTrie(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.end] = string

    def autoComplete(self, prefix):
        node = self.root
        for letter in prefix:
            if letter not in node:
                return []
            node = node[letter]
        words = []
        self._dfsHelper(node, words)
        return words

    def _dfsHelper(self, node, words):
        for letter in node:
            if letter == self.end:
                words.append(node[self.end])
                continue
            self._dfsHelper(node[letter], words)
        return words

# O(ns + p + v + e) time | O(ns) space
# n = number of strings | s = length of the largest strings | p = length of the prefix | v = number of vertices | e = number of edges 
if __name__ == "__main__":
    trie = Trie()
    strings = [
        "Dog",
        "Do",
        "Cat",
        "Cow",
    ]
    for string in strings:
        trie.prepareTrie(string)
    
    print(trie.autoComplete("Do"))