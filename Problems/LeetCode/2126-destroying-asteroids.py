class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for ass in asteroids:
            if mass >= ass:
                mass += ass
            else:
                return False
        return True