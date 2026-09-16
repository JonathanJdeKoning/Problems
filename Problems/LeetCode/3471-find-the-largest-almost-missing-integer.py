class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        fq = Counter(nums)
        if len(nums) == 1: return nums[0]
        if k == len(nums): return max(nums)
        if k == 1: 
            ans = -1
            for num in nums:
                if fq[num] == 1:
                    ans = max(ans, num)
            return ans
        x = nums[0]
        y = nums[-1]
        if nums.count(x) > 1 and nums.count(y) == 1: return y
        if nums.count(x) == 1 and nums.count(y) > 1: return x
        if nums.count(x) == 1 and nums.count(y) == 1: return max(x, y)
        return -1