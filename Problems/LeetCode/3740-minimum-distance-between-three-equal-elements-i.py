class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mp = defaultdict(list)
        for i, num in enumerate(nums):
            mp[num].append(i)
        ans = inf
        for k,v in mp.items():
            if len(v) < 3: continue

            for i in range(len(v)-2):
                a, b, c = v[i], v[i+1], v[i+2]
                ans = min(ans, abs(a-b)+abs(b-c)+abs(a-c))
        

        return ans if ans != inf else -1