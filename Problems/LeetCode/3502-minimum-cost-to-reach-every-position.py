class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans = []
        for i in range(len(cost)):
            ans.append(min(cost[:i+1]))
        return ans