class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        return num in [i+int(str(i)[::-1]) for i in range(num+1)]