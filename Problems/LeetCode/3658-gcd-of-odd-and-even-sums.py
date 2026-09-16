class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0
        for i in range(1,n*2,2):
            sumOdd += i
            sumEven += i+1
        return gcd(sumOdd, sumEven)

