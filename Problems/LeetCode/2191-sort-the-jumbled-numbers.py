class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda z:int("".join([str(mapping[int(x)]) for x in str(z)])))

