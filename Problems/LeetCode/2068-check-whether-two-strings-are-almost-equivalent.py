class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        words1, words2 = {}, {}
        alph = "abcdefghijklmnopqrstuvwxyz"
        for c in alph:
            words1[c] = 0
            words2[c] = 0

        for c in word1:
            words1[c] += 1
        for c in word2:
            words2[c] += 1

        for c in alph:
            if abs(words1[c] - words2[c]) > 3:
                return False
        return True
        