class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [sorted([(x.count(1),i) for i, x in enumerate(mat)])[i][1] for i in range(k)]