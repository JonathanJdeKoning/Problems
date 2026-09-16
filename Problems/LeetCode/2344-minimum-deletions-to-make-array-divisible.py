class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = numsDivide[0]
        for num in numsDivide[1:]:
            g = gcd(g, num)
        print(g)
        nums.sort()
        ans = 0
        for num in nums:
            if g % num != 0:
                ans += 1
            else:
                return ans
        return -1