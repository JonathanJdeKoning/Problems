class Solution:
    def numOfBurgers(self, t: int, c: int) -> List[int]:
        x = -c + t/2
        y = 2*c - t/2
        if x < 0 or y < 0: return []
        if not x.is_integer() or not y.is_integer(): return []
        return [int(x), int(y)]