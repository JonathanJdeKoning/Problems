class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        orig = num
        if num == 0:
            return True
        return str(orig) == str(num)[::-1].strip("0")[::-1]