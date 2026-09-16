class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        total = 0
        for num1 in arr1:
            if len([x for x in arr2 if abs(x-num1)<=d]) == 0: total += 1
        return total