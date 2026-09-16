class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        fq = Counter(nums)
        ans = 0
        for key, val in fq.items():
            if val % k == 0:
                ans += key*val
        return ans