class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        badIndices = [i for i in range(len(s1)) if s1[i] != s2[i]]
        if len(badIndices) == 0: return True
        if len(badIndices) != 2: return False
        i,j = badIndices
        return s1[i] == s2[j] and s1[j] == s2[i]