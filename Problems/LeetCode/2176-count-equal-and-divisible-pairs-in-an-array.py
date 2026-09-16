class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        total = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j >= i: continue
                if nums[i]== nums[j] and (i*j)%k == 0:total += 1
        return total