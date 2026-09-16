class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            do = set()
            de = set()
            for j in range(i, len(nums)):
                if nums[j] % 2 == 0:
                    de.add(nums[j])
                else:
                    do.add(nums[j])
                if len(de) == len(do):
                    ans = max(ans, j-i+1)
        return ans

                
                