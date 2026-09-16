class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
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
        
        total = 0
        for i in range(left,right+1):
            if is_prime(bin(i).count("1")): total += 1
        return total
