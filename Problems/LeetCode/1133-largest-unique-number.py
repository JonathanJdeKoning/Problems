class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        fq = Counter(nums)
        ans = -1
        for k,v in fq.items():
            if v == 1:
                ans = max(ans, k)
        return ans