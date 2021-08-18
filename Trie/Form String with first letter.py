class Trie:
    def __init__(self, string):
        self.root = {}
        self.end = "*"
        self._buildTrie(string)

    def _buildTrie(self, string):
        node = self.root
        for letter in string:
            if letter is " ":
                node[self.end] = True
                node = self.root
                continue

            if letter not in node:
                node[letter] = {}
            node = node[letter]

    def create(self):
        node = self.root
        string = ""
        for letter in node.keys():
            string = string + letter
        return string

def create(string):
    stri = string[0]
    for i in range(len(string)):
        if string[i] == " ":
            stri = stri + string[i + 1]
    return stri

    
t = Trie("This is a big string")
print(t.create())
print(create("This is a big string"))