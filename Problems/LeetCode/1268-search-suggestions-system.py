
class Trie:
    def __init__(self, *words):
        self.root = {}
        for word in words:
            self.add(word)

    def add(self, word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict["_end_"] = True

    def __contains__(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return "_end_" in current_dict

    def __delitem__(self, word):
        current_dict = self.root
        nodes = [current_dict]
        for letter in word:
            current_dict = current_dict[letter]
            nodes.append(current_dict)
        del current_dict["_end_"]

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        ans = []
        pref = []
        arr = []
        for word in products:
            trie.add(word)
        def trav(head):
            nonlocal arr
            if len(arr) == 3: return

            if "_end_" in head:
                arr.append("".join(pref))
            if len(arr) == 3: return

            for k in head.keys():
                if k != "_end_":
                    pref.append(k)
                    trav(head[k])
                    pref.pop()
            
        for newChar in searchWord:
            pref.append(newChar)
            arr = []
            head = trie.root
            bad = False
            for c in pref:
                if c in head:
                    head = head[c]
                else:
                    ans.append(arr)
                    bad = True
                    break
            if not bad:
                trav(head)
                ans.append(arr)
        return ans