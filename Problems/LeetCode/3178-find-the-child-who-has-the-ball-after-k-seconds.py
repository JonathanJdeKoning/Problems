class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        kid = 0
        up = True
        for i in range(k):
            if up:
                kid += 1
            else:
                kid -= 1
            if kid == 0:
                up = True
            elif kid == n-1:
                up = False
        return(kid)