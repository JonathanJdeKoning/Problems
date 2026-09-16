class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        @cache
        def pp(x, n):
            
            if n == 0: return 1
            if n == 1: return x
            if n%2==0: return pp(x, n//2)*pp(x, n//2)
            if n%2==1: return pp(x, n//2)*pp(x, n//2+1)
        
        ans = pp(x, abs(n))
        if n < 0:
            return 1/ans
        return ans