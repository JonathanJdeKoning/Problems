class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        t = sum(nums)
        a = 0
        while t %k!= 0:
            t-= 1
            a += 1
        return a