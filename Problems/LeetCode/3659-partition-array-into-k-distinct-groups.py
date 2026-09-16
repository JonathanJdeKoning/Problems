class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        fq = Counter(nums)
        if len(nums) % k != 0: return False
        groups = len(nums) // k
        return not [x for x in fq.values() if x > groups]