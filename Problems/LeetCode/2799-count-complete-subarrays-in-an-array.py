class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        D = len(set(nums))
        ans = 0
        for i in range(len(nums)):
            S = set()
            for j in range(i+1, len(nums)+1):
                S.add(nums[j-1])
                if len(S) == D:
                    ans += 1
        return ans