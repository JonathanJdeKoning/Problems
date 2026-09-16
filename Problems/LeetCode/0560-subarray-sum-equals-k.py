class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        d = defaultdict(int)
        d[0] = 1
        pref = 0
        for num in nums:
            pref += num
            res += d[pref-k]
            d[pref] += 1
        return res