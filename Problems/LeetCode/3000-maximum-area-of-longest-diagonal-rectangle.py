class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        bestDiag = 0
        bestArea = 0
        for l, w in dimensions:
            diag = l*l + w*w
            area = l*w
            if diag >= bestDiag:
                if diag == bestDiag:
                    bestArea = max(area, bestArea)
                else:
                    bestArea = area
                bestDiag = diag

        return bestArea