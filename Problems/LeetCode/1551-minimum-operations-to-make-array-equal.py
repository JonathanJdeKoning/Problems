class Solution:
    def minOperations(self, n: int) -> int:
        mx = n*2-1
        base = (mx+1)//2
        ans = 0
        for i in range(1, base+1,2):
            ans += abs(i-base)

        return ans
