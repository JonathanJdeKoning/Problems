class Solution:
    def sumZero(self, n: int) -> List[int]:
        out = []
        if n%2!=0: 
            out.append(0)
            n -=1
        for i in range(1,1+(n//2)):
            out.append(i)
            out.append(-i)
        return out