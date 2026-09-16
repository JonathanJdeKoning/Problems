class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = int(1e9) + 7
        R, C = len(mat), len(mat[0])
        if R == 1: return mat[0].count(1)
        
        @cache
        def coprimeWays(row, currGCD):
            if row == R-1:
                ways = 0
                for num in mat[row]:
                    if gcd(currGCD, num) == 1:
                        ways += 1
                return ways

            ways = 0
            for num in mat[row]:
                ways += coprimeWays(row+1, gcd(currGCD, num))
            return ways % MOD
                

        ans = 0
        for num in mat[0]:
            ans += coprimeWays(1, num)
        return ans % MOD