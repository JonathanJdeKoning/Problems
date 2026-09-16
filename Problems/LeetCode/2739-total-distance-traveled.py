class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        miles = 0
        used = 0 
        while mainTank > 0:
            mainTank -=1
            miles += 10
            used +=1
            if used == 5:
                used = 0
                if additionalTank > 0:
                    mainTank += 1
                    additionalTank -= 1
        return miles