class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        ans = []

        prev = lower-1
        for num in nums:
            if num != prev + 1:
                ans.append([prev+1, num-1])
            prev = num
        if prev != upper:
            ans.append([prev+1, upper])
        return ans

