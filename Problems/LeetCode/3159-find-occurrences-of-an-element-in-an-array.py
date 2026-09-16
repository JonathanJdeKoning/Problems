class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        a = []
        for i, num in enumerate(nums):
            if num == x:
                a.append(i)
        n = len(a)
        out = []
        for q in queries:
            if q > n:
                out.append(-1)
                continue
            out.append(a[q-1])
        return out