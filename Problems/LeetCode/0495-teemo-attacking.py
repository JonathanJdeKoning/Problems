class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0: return 0
        mp = defaultdict(int)
        for t in timeSeries:
            mp[t] += 1
            mp[t+duration] -= 1

        ans = 0
        prev = 0
        curr = 0
        clean = True
        print(mp)
        for k in sorted(list(mp.keys())):
            curr += mp[k]
            if curr>0:
                if clean:
                    clean = False
                else:
                    ans += k - prev
            else:
                ans += k - prev
                clean = True
            prev = k

        return ans
