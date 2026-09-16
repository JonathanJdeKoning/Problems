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
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ans = 0
        for i in range(len(nums)):
            if is_prime(nums[i][i]):
                ans = max(ans, nums[i][i])
            if is_prime(nums[(len(nums) - 1)- i][i]):
                ans = max(ans, nums[(len(nums) - 1) -i][i])
        return ans