class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes = []
        def is_prime(n):
            if n < 2: 
                return False
            if n % 2 == 0:             
                return n == 2
            k = 3
            while k*k <= n:
                if n % k == 0:
                    return False
                k += 2
            return True
        for i in range(1000):
            if is_prime(i): primes.append(i)

        ans = []
        for num in nums:
            if is_prime(num): ans.append(num); continue

            for i in range(2,num):
                if num%i==0 and is_prime(i):
                    ans.append(i)
        print(ans)
        return len(set(ans))