class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(key=abs) 
        elems = nums[-3:]
        if elems.count(0) >= 2: return 0
        return abs(int(1e5)* reduce(lambda a,b: a*b, elems[-2:]))