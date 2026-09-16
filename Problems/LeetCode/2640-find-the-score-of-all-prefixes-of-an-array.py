class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans = []
        mx = 0
        tot = 0
        for num in nums:
            mx = max(mx, num)
            tot += num+mx
            ans.append(tot)
        return ans