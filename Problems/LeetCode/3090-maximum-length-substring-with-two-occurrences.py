class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0 
        r = 0
        ans = 1
        fq = Counter()
        while r < len(s):
            fq[s[r]] += 1
            while fq[s[r]] == 3:
                fq[s[l]] -=1
                l += 1
            ans = max(ans, sum(fq.values()))
            r+= 1



        return ans   