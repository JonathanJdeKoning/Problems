class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return len([x for x in list(Counter(nums).values()) if x%2!= 0]) == 0