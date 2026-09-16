class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        aTotal, bTotal = 0, 0
        
        for drinkA, drinkB in zip(energyDrinkA, energyDrinkB):

            aTotal, bTotal = max(aTotal + drinkA, bTotal), max(bTotal + drinkB, aTotal)

        return max(aTotal, bTotal)