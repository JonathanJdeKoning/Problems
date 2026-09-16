class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pfq = Counter(p)
        ans = []
        l = 0
        r = len(p)
        sfq = Counter(s[l:r])
        while r <= len(s):
            if sfq == pfq:
                ans.append(l)
            if r == len(s): break
            sfq[s[l]] -= 1
            sfq[s[r]] += 1
            l += 1
            r += 1
        return ans
        