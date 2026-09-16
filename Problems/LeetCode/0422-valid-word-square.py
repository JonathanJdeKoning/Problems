class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        R, C = len(words), len(words[0])

        mxLen = len(max(words, key=len))
        for i, word in enumerate(words):
            words[i] = word.ljust(mxLen, ">")
            print(words[i])
        
        for i in range(R):
            row = list(words[i])
            col = [r[i] for r in words]
            if row != col:
                return False
        return True
        