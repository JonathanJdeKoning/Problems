class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return Counter(nums).most_common()[0][1] >= 2
