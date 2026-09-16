class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        t = {i+1:c for i,c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
        t[0] = "Z"
        del t[26]
        ans = []

        while columnNumber>0:
            mod = columnNumber%26
            ans.append(t[mod])
            columnNumber//=26
            if mod == 0: columnNumber -=1
            
        return "".join(ans[::-1])