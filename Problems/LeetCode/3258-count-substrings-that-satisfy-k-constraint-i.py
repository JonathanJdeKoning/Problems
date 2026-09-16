class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                chk = s[i:(j+1)]
                if chk.count("1") <= k or chk.count("0") <= k:
                    ans += 1
        return ans
