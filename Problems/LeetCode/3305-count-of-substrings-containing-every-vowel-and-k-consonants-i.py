class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def allsubs(x): return [x[i:j] for i in range(len(x)) for j in range(i+1,len(x)+1)]
        subs = allsubs(word)
        ans = 0
        for sub in subs:
            if "a" in sub and "e" in sub and "i" in sub and "o" in sub and "u" in sub:
                if len([x for x in sub if x not in "aeiou"]) == k:
                    ans += 1
        return ans