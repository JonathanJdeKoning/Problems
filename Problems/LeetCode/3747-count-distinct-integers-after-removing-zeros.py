class Solution:
    def countDistinct(self, n: int) -> int:
        s = str(n)
        m= floor(log(n, 10))
        k = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                k = len(s) - i - 1
        print(f"{k=}")
        if n < 10: return n
        def b(n,k):
            return floor(n/10**k)*10**k
        if k == 0:
            return n - 1 - sum([floor((b(n,k+1)-1)/10**j)*9**(j-1) for j in range(1, m+1)])
        else:
            return b(n,k) - 1 - sum([floor((b(n,k)-1)/10**j)*9**(j-1) for j in range(1, m+1)])