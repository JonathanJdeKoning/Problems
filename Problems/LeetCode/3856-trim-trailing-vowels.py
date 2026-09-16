class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        s = list(s)
        v = "aeiou"

        while s:
            if s[-1] in v:
                s.pop()
            else:
                break
        return "".join(s)        