class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        m = 2**(n)
        k -= 1
        swaps =1
        while m:
            m //= 2
            if k >= m:
                swaps += 1
                k -= m
        return swaps%2
