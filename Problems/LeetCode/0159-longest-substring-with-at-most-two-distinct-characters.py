class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l=0
        fq = defaultdict(int)
        fq[s[l]] += 1
        ans = 1

        for r in range(1, len(s)):
            fq[s[r]] += 1
            
            while len(fq) > 2:
                fq[s[l]] -= 1
                if fq[s[l]] == 0:
                    del fq[s[l]]
                l += 1
            ans = max(ans, (r-l)+1 )
        return ans