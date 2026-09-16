class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mxLen = 0
        l = 0
        r = 0
        seen = set()
        while r < len(s):
            c = s[r]
            while c in seen:
                seen.discard(s[l])
                l += 1
            seen.add(c)
            mxLen = max(mxLen, r - l + 1)
            
            r += 1
        return mxLen
            
                


