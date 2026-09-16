class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        mod = int(1e9+7)

        def upto(n):
            return (n*(n+1)) // 2

        def rangeSum(s,e):
            return (upto(e) - upto(s-1))
        
        ans = upto(target//2) + rangeSum(target, target+(n-(target//2+1)))
        if n + (n-1) < target:
            ans = upto(n)
        return int(ans % mod)



        
            