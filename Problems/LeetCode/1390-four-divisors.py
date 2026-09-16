class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
        ans = 0
        for num in nums:
            f = factors(num)
            if len(f) == 4:
                ans += sum(f)
        return ans