class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        r = []
        pref = 0
        for n in shifts[::-1]:
            r.append((n+pref)%26)
            pref += n
        r = r[::-1]

        return("".join([    chr((((ord(s[i])-97)+r[i])%26)+97)     for i, c in enumerate(s)]))