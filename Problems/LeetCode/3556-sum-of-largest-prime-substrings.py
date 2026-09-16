class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        
        def is_prime(n):
            if n < 2: 
                return False;
            if n % 2 == 0:             
                return n == 2
            k = 3
            while k*k <= n:
                if n % k == 0:
                    return False
                k += 2
            return True
        A = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = int(s[i:j+1])
                if is_prime(sub):
                    A.append(sub)
        A = sorted(set(A))
        if len(A) <= 3:
            return sum(A)

        ans = 0
        for _ in range(3):
            ans += A.pop()
        return ans