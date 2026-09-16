class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalLength = sum(matchsticks)
        if totalLength%4 != 0: return False
        sideLength = totalLength // 4

        matchsticks.sort(reverse=True)

        @cache
        def canMakeSquare(i, a, b, c, d):     
            if i == len(matchsticks):
                return len(set([a, b, c, d])) == 1
            
            num = matchsticks[i]
            if a + num <= sideLength:
                if canMakeSquare(i+1, a+num, b, c, d): return True

            if b + num <= sideLength:
                if canMakeSquare(i+1, a, b+num, c, d): return True

            if c + num <= sideLength:
                if canMakeSquare(i+1,a, b, c+num, d): return True

            if d + num <= sideLength:
                if canMakeSquare(i+1, a, b, c, d+num): return True
            return False
            
        return canMakeSquare(0, 0, 0, 0, 0)





