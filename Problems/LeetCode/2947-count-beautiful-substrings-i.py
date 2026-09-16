class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = set(list("aeiou"))
        ans = 0
        for i in range(len(s)):
            v = 0
            c = 0

            for j in range(i, len(s)):
                if s[j] in vowels:
                    v += 1
                else:
                    c += 1

                if v != c: continue

                if (v*c) % k == 0:
                    ans += 1

        return ans 