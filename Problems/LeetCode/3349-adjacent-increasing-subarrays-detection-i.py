class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        l = 0
        r = k
        while r+k <= len(nums):
            for i in range(1, k):
                if nums[l+i] > nums[l+i-1] and nums[r+i] > nums[r+i-1]:
                    continue
                else:
                    l +=1
                    r += 1
                    break
            else:
                return True

        return False
