class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            for i in range(num):
                if i | (i+1) == num:
                    ans.append(i)
                    break
            else:
                ans.append(-1)
        return ans