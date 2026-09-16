class Solution:
    def convertToBase7(self, num: int) -> str:
        def numberToBase(n, b):

            if n == 0:
                return [0]
            
            digits = []
            neg = False
            if n < 0:
                n = -n
                neg = True
            while n:
                digits.append(int(n % b))
                n //= b
            if neg: digits.append("-")
            return digits[::-1]
        return "".join([str(x) for x in numberToBase(num,7)])