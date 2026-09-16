class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
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
        
        r = nums[::-1]
        mn = None
        mx = None
        for i,num in enumerate(nums):
            if is_prime(num):
                mn = i
                break
        for i,num in enumerate(r):
            if is_prime(num):
                mx = len(r)-i-1
                break
        return abs(mx-mn)
                
        