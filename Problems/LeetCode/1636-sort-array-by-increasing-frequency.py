class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        fq = Counter(nums)
        return sorted(nums, key=lambda x: (fq[x],-x))
