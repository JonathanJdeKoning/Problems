class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        ans = comb(N, 2)
        fq = Counter()
        for i in range(len(nums)):
            fq[i - nums[i]] += 1
        for v in list(fq.values()):
            ans -= comb(v, 2)

        return ans

