class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        poss = set()
        for i in range(len(nums)-1):
            s = nums[i]+nums[i+1]
            if s in poss:
                return True
            else:
                poss.add(s)
        return False