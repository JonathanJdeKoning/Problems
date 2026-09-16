class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set() 
        while True:
            if 1 in nums:
                return True
            else:
                total = 0
                for c in str(n):
                    total += int(c)**2
                if total in nums:
                    return False
                else:
                    nums.add(total)
                    n = total