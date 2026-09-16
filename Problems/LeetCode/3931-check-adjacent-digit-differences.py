class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        return all(abs(int(x)-int(y))<=2 for x, y in pairwise(s))