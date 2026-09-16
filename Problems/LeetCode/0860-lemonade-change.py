class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f = 0
        t = 0
        for bill in bills:
            if bill == 5:
                f += 1
            elif bill == 10:
                if not f: return False
                f -= 1
                t += 1
            elif bill == 20:
                if t and f:
                    t -= 1
                    f -= 1
                elif f >= 3:
                    f -= 3
                else:
                    return False
        return True



