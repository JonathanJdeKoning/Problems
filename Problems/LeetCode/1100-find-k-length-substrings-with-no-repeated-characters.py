class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s): return 0
        ans = 0 
        l = 0
        r = k
        fq = Counter(s[l:r])
        reps = len([x for x in list(fq.values()) if x > 1])
        if not reps:
            ans = 1
        if k == len(s):
            return ans
        print(ans)
        while True:
            fq[s[l]] -= 1
            l += 1

            fq[s[r]] += 1
            r += 1
            if not [x for x in list(fq.values()) if x > 1]:
                ans += 1
            if r == len(s): break

        return ans
                