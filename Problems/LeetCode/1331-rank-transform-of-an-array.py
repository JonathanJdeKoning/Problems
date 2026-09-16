class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        mp = {k: i+1 for i, (k,v) in enumerate(groupby(sorted(arr)))}
        return list(map(lambda x:mp[x], arr))
