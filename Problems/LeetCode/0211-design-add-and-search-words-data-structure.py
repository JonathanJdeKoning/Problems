
class WordDictionary:

    def __init__(self):
        self.T = {}                

    def addWord(self, word: str) -> None:
        curr = self.T
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["end"] = True


    def search(self, word: str, start=None, startI=0) -> bool:

        if start is None:
            curr = self.T
        else:
            curr = start
        #print(word, startI, start)
        for i, c in enumerate(word, start=startI):
            if c == ".":
                for d in curr:
                    if d == "end": continue
                    if self.search(word[(i-startI)+1:], curr[d], i+1):
                        return True
                return False

            if c not in curr: return False
            curr = curr[c]
        return "end" in curr

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)