class Solution:
    def isFascinating(self, n: int) -> bool:
        new = str(n) + str(n*2) + str(n*3)
        return sorted(new) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']