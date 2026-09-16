class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = dict(Counter(arr)).items()
        mx = -1
        for k, v in count:
            if k==v: mx = max(mx, k)
        return mx