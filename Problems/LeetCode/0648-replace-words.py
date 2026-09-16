class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for c in word:
            idx = ord(c)-97

            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.end = True


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tri = Trie()
        for word in dictionary:
            tri.add(word)

        out = []
        for word in sentence.split():
            curr = tri.root
            trace = []
            for c in word:
                idx = ord(c)-97
                if not curr.children[idx]:
                    trace = [word]
                    break
                curr = curr.children[idx]
                trace.append(c)
                if curr.end: break
            out.append("".join(trace))
        return(" ".join(out))
            
        
 
