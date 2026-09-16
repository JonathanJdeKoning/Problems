class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        
        @cache 
        def min_cost(hStart, hEnd, vStart, vEnd):
            if hStart==hEnd and vStart==vEnd: return 0

            mn = inf
            for i in range(hStart,hEnd):
                sliceCost = horizontalCut[i]
                startSeg = min_cost(hStart,i, vStart, vEnd)
                endSeg = min_cost(i+1, hEnd,vStart,vEnd)
                
                mn = min(mn, sliceCost+startSeg+endSeg)

            for i in range(vStart,vEnd):
                sliceCost = verticalCut[i]
                startSeg = min_cost(hStart, hEnd, vStart, i)
                endSeg = min_cost(hStart,hEnd, i+1, vEnd)
                
                mn = min(mn, sliceCost+startSeg+endSeg)
            return mn
        return min_cost(0, m-1, 0, n-1)




