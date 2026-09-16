class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        count = 0
        curr = 0
        for num in nums:
            
            curr += num
            if curr > 0:
                count += 1
            else:
                break
        return count


