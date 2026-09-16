class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        new1 = ""
        new2 = ""
        for s in word1:
            new1 += s
        for s in word2:
            new2 += s
        return new1 == new2