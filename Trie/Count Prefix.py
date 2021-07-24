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

    def search(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.end in node

    def printTrie(self):
        node = self.root
        array = []
        self._dfsHelper(array, node)
        return array

    def _dfsHelper(self, array, node):
        for letter in node:
            if letter == self.end:
                array.append(node[self.end])
                continue
            self._dfsHelper(array, node[letter])
        return array

    def countPrefix(self, prefix):
        node = self.root
        for letter in prefix:
            if letter not in node:
                return 0
            node = node[letter]
        words = []
        self._dfsHelper(words, node)
        return len(words)
        
# O(ns + p + v + e) time | O(ns) space
# n = number of strings | s = length of the largest strings | p = length of the prefix | v = number of vertices | e = number of edges
if __name__ == "__main__":
    trie = Trie()
    trie.prepareTrie("Dog")
    trie.prepareTrie("Doom")
    trie.prepareTrie("Cat")
    trie.prepareTrie("Doll")
    print(trie.search("Dog"))
    print(trie.printTrie())
    print(trie.countPrefix("Do"))

        