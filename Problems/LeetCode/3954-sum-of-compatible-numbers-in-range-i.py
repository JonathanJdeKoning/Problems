class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        ans = 0
        for i in range(max(n-k, 0), n+k+1):
            if i&n == 0:
                ans += i
        return ans
