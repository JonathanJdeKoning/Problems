class Solution:
    def minSwaps(self, s: str) -> int:
        x = y = 0
        for c in s:
            if c == "[": 
                x += 1
                continue
            if not x: y += 1
            else:     x -= 1
        return((y+1)//2) 