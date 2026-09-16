class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a,b,c = sorted([a,b,c])
        if c == b+1 and b == a+1:
            return [0,0]
        if b == c-2 or b == a+2 or c==b+1 or b==a+1:
            mn = 1
        else:
            mn = 2

        return [mn, ((c-b)-1) + ((b-a)-1)]