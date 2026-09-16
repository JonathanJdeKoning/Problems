class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        out = []
        for i in range(len(s)//2):
            left = s[i]
            right = s[-(i+1)]

            if left < right: out.append(left)
            else: out.append(right)
        out.extend(out[::-1])
        if len(s)%2==1:
            out.insert(len(out)//2,s[len(s)//2])
        return "".join(out)