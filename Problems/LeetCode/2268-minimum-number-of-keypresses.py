class Solution:
    def minimumKeypresses(self, s: str) -> int:
        fq = Counter(s)
        q = deque([1]*9)
        ans = 0
        mp = {}
        for c, v in fq.most_common():
            if c not in mp:
                cnt = q.pop()
                q.appendleft(cnt+1)
                mp[c] = cnt
            ans += v * mp[c]
        return ans
