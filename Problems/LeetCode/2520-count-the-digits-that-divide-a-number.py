class Solution:
    def countDigits(self, num: int) -> int:
        return len([x for x in str(num) if num%int(x) == 0])