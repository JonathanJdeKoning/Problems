class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        mp = {"a":"z"}
        alph = "abcdefghijklmnopqrstuvwxyz"
        for i, c in enumerate(alph[1:], start = 1):
            mp[c] = alph[i-1]
        
        currS = 0
        currT = 0

        while True:
            s = str1[currS]
            t = str2[currT]
            if s == t or s == mp[t]:
                currT += 1
            currS += 1

            if currT == len(str2): return True
            if currS == len(str1): return False 