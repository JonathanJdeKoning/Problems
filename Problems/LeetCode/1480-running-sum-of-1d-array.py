class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        curr = 0
        for num in nums:
            curr+= num
            ans.append(curr)
        return ans