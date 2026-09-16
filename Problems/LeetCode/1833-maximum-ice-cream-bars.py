class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total = 0
        for cream in costs:
            if cream <= coins:
                coins -= cream
                total += 1
            else:
                return total
        return total