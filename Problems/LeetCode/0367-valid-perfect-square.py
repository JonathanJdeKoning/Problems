class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1 or num == 4: return True

        l = 0
        r = num//2

        while l <= r:
            mid = (l+r)//2
            
            sqr = mid*mid
            if sqr == num: return True

            if sqr > num:
                r = mid-1
            else:
                l = mid+1
        return False
            
