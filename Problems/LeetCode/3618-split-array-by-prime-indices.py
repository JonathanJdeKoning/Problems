class Solution:
    def is_prime(self, n):
        if n < 5 or n & 1 == 0 or n % 3 == 0:
            return 2 <= n <= 3
        s = ((n - 1) & (1 - n)).bit_length() - 1
        d = n >> s
        for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
            p = pow(a, d, n)
            if p == 1 or p == n - 1 or a % n == 0:
                continue
            for _ in range(s):
                p = (p * p) % n
                if p == n - 1:
                    break
            else:
                return False
        return True
    def splitArray(self, nums: List[int]) -> int:
        A = 0
        B = 0

        for i, num in enumerate(nums):
            if self.is_prime(i):
                A += num
            else:
                B += num
        return abs(A-B)
        