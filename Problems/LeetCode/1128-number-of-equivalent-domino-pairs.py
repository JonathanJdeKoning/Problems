class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        old = defaultdict(int)
        for dom in dominoes:
            old["".join([str(x) for x in sorted(dom)])] += 1
        return int(sum([(i-1)*((i)/2) for i in old.values()]))
        
            

