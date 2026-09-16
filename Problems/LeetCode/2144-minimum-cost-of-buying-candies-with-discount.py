class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        heapify_max(cost)
        ans = 0
        while cost:
            ans += heappop_max(cost)
            if cost: ans += heappop_max(cost)
            if cost: heappop_max(cost)
        return ans