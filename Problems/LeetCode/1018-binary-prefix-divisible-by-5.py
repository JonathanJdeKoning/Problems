class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        curr = 0
        ans = []
        for num in nums:
            curr = curr*2+num
            ans.append(curr%5==0)
        return ans
