class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if nums.count(0) == 0: return len(nums)
        ans = 1
        groups = []
        for k, v in groupby(nums):
            groups.append((k, len(list(v))))
        for i, (k, v) in enumerate(groups):
            if k == 1:
                ans = max(ans, v + 1)
            elif k == 0 and v == 1 and i != 0 and i != len(groups) - 1:
                ans= max(ans, 1+ groups[i-1][1] + groups[i+1][1])
        return ans