class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        arr.sort()
        gap = min(arr[1] - arr[0], arr[-1] - arr[-2])
        if gap == 0: return arr[0]
        for a,b in pairwise(arr):
            if b - a != gap:
                return a + gap