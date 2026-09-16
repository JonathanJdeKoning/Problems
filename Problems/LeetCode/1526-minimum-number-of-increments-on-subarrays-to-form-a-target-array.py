class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        return sum(max(0,b-a) for a,b in pairwise([0] + target))        

    

