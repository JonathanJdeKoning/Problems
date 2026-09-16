class Solution:
    def sumBase(self, n: int, k: int) -> int:
        def numberToBase(n, b):
            if n == 0:
                return [0]
            digits = []
            while n:
                digits.append(int(n % b))
                n //= b
            return digits[::-1]
        return sum(numberToBase(n,k))