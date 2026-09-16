class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        totalCost = sum(cost)
        costMP = {}
        for c, n in zip(s, cost):
            if c not in costMP:
                costMP[c] = totalCost
            costMP[c] -= n
        return min(costMP.values())