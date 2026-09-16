class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for num in range(low, high+1):
            s = str(num)
            if len(s)%2==1: continue
            mid = len(s) // 2
            if sum([int(x) for x in s[:mid]]) == sum([int(x) for x in s[mid:]]):
                ans +=1
        return ans
