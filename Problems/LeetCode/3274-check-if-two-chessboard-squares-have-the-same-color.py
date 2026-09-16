class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        r1, c1 = coordinate1
        r2, c2 = coordinate2
        return (ord(r1)-96 + int(c1))%2 == (ord(r2)-96 + int(c2))%2