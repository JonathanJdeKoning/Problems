class Solution:
    def numberCount(self, a: int, b: int) -> int:
        ans = 0
        for i in range(a, b+1):
            s = str(i)
            if len(s) == len(set(s)):
                ans += 1
        return ans