class Solution:
    def findScore(self, nums: List[int]) -> int:
        h = []
        bad = set()
        for i, num in enumerate(nums):
            heappush(h,(num, i))
        ans = 0
        while h:
            num, i = heappop(h)
            if i in bad: continue
            ans += num
            bad.add(i)
            bad.add(i-1)
            bad.add(i+1)
        return ans