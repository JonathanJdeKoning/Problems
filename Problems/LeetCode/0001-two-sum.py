class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lastSeenAt = {}
        N = len(nums)
        for i in range(N):
            num = nums[i]
            complement = target - num
            if complement in lastSeenAt:
                return [i, lastSeenAt[complement]]

            lastSeenAt[num] = i
            