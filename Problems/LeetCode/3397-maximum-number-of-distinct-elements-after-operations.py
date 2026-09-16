class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        fq = Counter(nums)
        ans = 0
        used = set()
        globmn = -inf
        for key, val in sorted(fq.items()):
            mn = max(key - k, globmn)
            mx = max(key + k, globmn)
            avail = (mx-mn)+1
            use = min(avail, val)
            globmn = mn +use
            ans += use
        return ans
            
            