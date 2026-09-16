class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        new = []
        for c in word:
            if c.isdigit():
                new.append(c)
            else:
                new.append(" ")
        new = [int(x) for x in "".join(new).split()]
        return len(set(new))