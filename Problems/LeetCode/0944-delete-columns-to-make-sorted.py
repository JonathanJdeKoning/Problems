class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        total = 0
        for i in range(len(strs[0])):
            col = [x[i] for x in strs]
            if col != sorted(col):
                total += 1
        return total