class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        need = (sum(aliceSizes) + sum(bobSizes))//2
        poss = set(bobSizes)
        tot = sum(aliceSizes)
        for num in aliceSizes:
            if need - (tot-num) in poss:
                return [num, need-(tot-num)]