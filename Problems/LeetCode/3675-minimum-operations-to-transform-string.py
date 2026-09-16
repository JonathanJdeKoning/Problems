class Solution:
    def minOperations(self, s: str) -> int:
        uniq = sorted(set(s))
        if uniq[0] == "a": uniq = uniq[1:]
        ans =0 
        if not uniq: return ans
        for a,b in pairwise(uniq):
            ans += ord(b) - ord(a)
        ans += (ord("z")+1) - ord(uniq[-1])
        return ans