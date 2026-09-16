class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        mx = 0
        for i in range(1,26):
            if "0"*i+"1"*i in s:
                mx = i*2
        return mx