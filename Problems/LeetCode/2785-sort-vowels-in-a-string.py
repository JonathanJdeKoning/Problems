class Solution:
    def sortVowels(self, s: str) -> str:
        vows = sorted([x for x in s if x in "aeiouAEIOU"],reverse=True)
        new = list(s)
        for i, c in enumerate(s):
            if c in "aeiouAEIOU":
                new[i] = vows.pop()
        return "".join(new)