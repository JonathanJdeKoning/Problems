class Solution:
    def smallestPalindrome(self, s: str) -> str:
        mid = ""
        fq = [0]*26
        new = []
        if len(s)%2 == 1: mid = s[len(s)//2]
        for c in s[:len(s)//2]:
            fq[ord(c)-97] += 1
        for i in range(len(fq)):
            new.extend([chr(i+97)]*fq[i])
        t = "".join(new)
        return t + mid + t[::-1]

        