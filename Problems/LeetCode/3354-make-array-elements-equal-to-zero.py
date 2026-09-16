class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        tot = sum(nums)
        curr =0 
        ans = 0
        for i, num in enumerate(nums):
            if num == 0:
                if abs(curr - (tot-curr)) == 0:
                    ans += 2
                elif abs(curr - (tot-curr)) == 1:
                    ans += 1
            else:
                curr += num
        return ans