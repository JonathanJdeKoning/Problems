class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        return [x for x in range(1, len(mountain)-1) if mountain[x-1]<mountain[x]>mountain[x+1]]
        
