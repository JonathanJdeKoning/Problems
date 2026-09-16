class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        h = n/2
        for i,v in enumerate(sorted(list(Counter(arr).values()), reverse=True), start = 1):
            n -= v
            if n <= h:
                return i