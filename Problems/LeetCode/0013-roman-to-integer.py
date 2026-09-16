class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0
        for i in range(len(s)-1):
            char, nextChar = s[i], s[i+1]

            if values[char] >= values[nextChar]:
                total += values[char]
            else:
                total -= values[char]
        
        return total + values[s[-1]]