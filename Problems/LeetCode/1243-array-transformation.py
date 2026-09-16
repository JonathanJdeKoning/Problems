class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        prev = arr
        while True:
            new = prev.copy()
            for i in range(1, len(prev) - 1):
                if prev[i] > prev[i-1] and prev[i] > prev[i+1]:
                    new[i] -= 1
                if prev[i] < prev[i-1] and prev[i] < prev[i+1]:
                    new[i] += 1
            if new == prev: return new
            prev = new
        