class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        mp= {0:0,1:1,2:1}
        return sum(mp[x%3] for x in nums)