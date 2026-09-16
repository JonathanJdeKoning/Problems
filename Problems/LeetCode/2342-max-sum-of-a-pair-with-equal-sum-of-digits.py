class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = -1
        buckets = defaultdict(int)
        for num in nums:
            sm = sum(int(c) for c in str(num))
            if buckets[sm]:
                ans = max(ans, buckets[sm] + num)
            buckets[sm] = max(buckets[sm], num)
        return ans
