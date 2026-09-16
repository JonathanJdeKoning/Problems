class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def convert(s):
            curr = 0 
            mp = {}
            ans = []
            for c in s:
                if c not in mp:
                    curr += 1
                    mp[c] = curr
                ans.append(mp[c])
            return ans

        return [x for x in words if convert(x) == convert(pattern)]


