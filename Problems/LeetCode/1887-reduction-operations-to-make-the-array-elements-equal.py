class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if len(set(nums)) == 1: return 0
        fq = Counter(nums)
        arr = sorted(fq.items(), reverse=True)
        ans = 0
        build = 0
        for num, cnt in arr[:-1]:
            build += cnt
            ans += build
        return ans

