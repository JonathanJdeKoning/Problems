class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        thirty = set([9, 4, 6, 11])
        if month in thirty: return 30
        if month != 2: return 31

        if year%400 ==0 :
            return 29
        if year % 100 == 0:
            return 28
        if year % 4 == 0:
            return 29
        return 28