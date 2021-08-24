

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie:

    root = None

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in word:
            if node.children[abs(ord(i) - ord("a"))] == None:
                node.children[abs(ord(i) - ord("a"))] = TrieNode()
            node = node.children[abs(ord(i) - ord("a"))]
        node.isEnd = True

    def search(self, word):
        node = self.root
        for i in word:
            if node.children[ord(i) - ord("a")] == None:
                return False
            node = node.children[ord(i) - ord("a")]

        return node.isEnd

    def startsWith(self, word):
        node = self.root
        for i in word:
            if node.children[ord(i) - ord("a")] == None:
                return False
            node = node.children[ord(i) - ord("a")]
        return True


t = Trie()
t.insert("apple")
t.insert("app")

print(t.startsWith("appe"))









