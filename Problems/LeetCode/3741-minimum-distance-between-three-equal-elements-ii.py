class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        for i, n in enumerate(nums):
            pos[n].append(i)

        ans = inf
        for k, v in pos.items():
            if len(v) < 3: continue
            for i in range(len(v) - 2):
                a,b,c =v[i:i+3]
                ans = min(ans, abs(a-b) + abs(b-c) + abs(a-c))


        if ans == inf: return -1
        return ans