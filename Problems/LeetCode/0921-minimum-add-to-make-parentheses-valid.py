class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        imb = 0
        x = 0
        for c in s:
            if c == "(":
                x += 1
            else:
                if x > 0:
                    x -= 1
                else:
                    imb +=1


        return imb + x
                
