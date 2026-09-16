class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                a = s[i:j]

                for k in range(len(t)):
                    for l in range(k, len(t)+1):
                        b = t[k:l]
                        c = a+b
                        if c == c[::-1]: ans = max(ans, len(c))
        return ans
