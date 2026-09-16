class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        out = "z"*10000
        letters = [c.lower() for c in licensePlate if c.isalpha()]
        for word in words:
            left = letters[:]
            for c in word:
                if c in left:
                    left.remove(c)
            if len(left) == 0:
                if len(word) < len(out):
                    out = word
        return out
