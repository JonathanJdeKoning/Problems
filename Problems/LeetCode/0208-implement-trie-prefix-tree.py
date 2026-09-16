class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        head = self.root
        for c in word:
            if c not in head:
                head[c] = {"end":False}
            head = head[c]
        head["end"] = True

    def search(self, word: str) -> bool:
        head = self.root
        for c in word:
            if c not in head: return False
            head = head[c]
        if not head["end"]: return False
        return True

    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for c in prefix:
            if c not in head: return False
            head = head[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)