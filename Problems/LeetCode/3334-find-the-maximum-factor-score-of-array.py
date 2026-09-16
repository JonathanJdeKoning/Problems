class Solution:
    def maxScore(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]**2
        mx = reduce(lambda x,y: lcm(x,y), nums) * reduce(lambda x,y: gcd(x,y), nums)
        for i in range(len(nums)):
            l = reduce(lambda x,y: lcm(x,y), nums[:i] + nums[i+1:])
            g = reduce(lambda x,y: gcd(x,y), nums[:i] + nums[i+1:])
            mx = max(mx, l*g)
        return mx

            

            