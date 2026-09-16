class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def distToA(c):
            pos = ord(c)-97
            return min(pos, 26-pos)
        currletter = -1
        new = []
        while True:
            currletter += 1
            if currletter == len(s): break
            letter = s[currletter]
            if k <= 0:
                new.append(letter)
                continue
                
            aDist = distToA(letter)
            if aDist <= k:
                new.append("a")
                k -= aDist
                continue
            else:
                new.append(chr(ord(letter)-k))
                k = 0
                continue
        return "".join(new)
                
            
            