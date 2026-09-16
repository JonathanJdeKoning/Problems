class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        N = len(nums)
        fq = Counter(nums)
        uniq = sorted(set(nums))
        ans = 0
        rem = 0
        for num in uniq:
            rem += fq[num]

            x = N - rem
            if x >= k:
                ans += fq[num]

        return ans 
