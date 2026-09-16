class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = 1000
        for num in range(1,9999999):
            if num <=0: continue
            sv = num
            for b in nums:
                sv += b
                if sv < 1:
                    break
            else:
                return num
