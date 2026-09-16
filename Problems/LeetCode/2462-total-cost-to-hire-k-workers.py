class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if k >= len(costs): return sum(costs)
        cost =0
        h = []
        for l in range(candidates):
            heappush(h, (costs[l], l))
        for r in range(len(costs)-1, (len(costs) -1) - candidates, -1):
            if r == l: break
            heappush(h, (costs[r], r))
        print(l, r)
        print(h)
        for _ in range(k):
            best, idx = heappop(h)
            cost += best
            if l == r or l == r-1: continue
            if idx <= l:
                l += 1
                heappush(h, (costs[l], l))
            elif idx >= r:
                r -= 1
                heappush(h,(costs[r], r))

        return cost