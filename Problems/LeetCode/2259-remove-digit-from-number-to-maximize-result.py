class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        mx = 0
        for i,c in enumerate(number):
            if c == digit:
                mx = max(mx, int(number[:i]+number[i+1:]))
        return str(mx)

