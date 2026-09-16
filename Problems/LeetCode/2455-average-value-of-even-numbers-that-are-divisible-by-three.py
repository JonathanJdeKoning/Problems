class Solution:
    def averageValue(self, nums: List[int]) -> int:
        arr = [x for x in nums if x%6==0]
        if not arr: return int(bool(arr))
        return sum(arr)//len(arr)