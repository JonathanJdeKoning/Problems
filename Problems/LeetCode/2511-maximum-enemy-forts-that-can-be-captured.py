class Solution:
    def captureForts(self, forts: List[int]) -> int:
        r = 0
        j = 0
        for i in range(len(forts)):
            if forts[i] != 0:
                if forts[j] == -forts[i]:
                    r = max(r, i - j - 1)
                j=i
        return r
