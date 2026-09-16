class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        fq = Counter(nums)
        ans = []
        for key, val in fq.items():
            ans += [key]*(min(val, k))


        return sorted(ans)

        