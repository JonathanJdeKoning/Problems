class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = defaultdict(int)
        for s in arr:
            d[s] += 1
        dist = [key for key,v in d.items() if v == 1]
        return dist[k-1] if len(dist)>=k else ""

