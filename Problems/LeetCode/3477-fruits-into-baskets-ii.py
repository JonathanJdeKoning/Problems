class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = [False] * len(baskets)
        for i, fruit in enumerate(fruits):
            for j in range(len(baskets)):
                if used[j] : continue
                if baskets[j] >= fruit:
                    used[j] = True
                    fruits[i] = 0
                    break
        return len(fruits) - fruits.count(0)
                