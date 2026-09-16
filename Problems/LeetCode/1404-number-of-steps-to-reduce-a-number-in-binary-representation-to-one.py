class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s,2)
        total = 0
        while n != 1:
            if n%2==0:
                n//=2
            else:
                n+=1
            total += 1
        return total