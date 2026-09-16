class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        rev = num[::-1]
        found = False
        for i in range(len(num)):
            if rev[i] in "13579":
                found = True
                break
        if not found: return ""
        real = len(num) - i - 1
        return num[:real+1]