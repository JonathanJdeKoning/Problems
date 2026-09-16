class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heapq.heapify(happiness)
        most = sorted(heapq.nlargest(k,happiness),reverse=True)
        total = 0
        
        for i, child in enumerate(most):
            res = child - i
            if res > 0:
                total += res
            else:
                break
        return total