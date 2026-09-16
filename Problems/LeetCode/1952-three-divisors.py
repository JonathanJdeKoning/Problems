class Solution:
    def isThree(self, n: int) -> bool:
        count = 2
        for i in range(2, n):
            if n%i == 0:
                count += 1
                if count > 3: return False
        if count == 3: return True
        return False