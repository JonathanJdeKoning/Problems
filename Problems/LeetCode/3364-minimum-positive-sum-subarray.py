class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mn = 999999999
        for i in range(len(nums)+1):
            for j in range(len(nums)+1):
                x = j-i
                if x < l or x > r: continue
                s = sum(nums[i:j])
                if s > 0:
                    mn = min(mn, s)

        if mn != 999999999:
            return mn
        else:
            return -1
        