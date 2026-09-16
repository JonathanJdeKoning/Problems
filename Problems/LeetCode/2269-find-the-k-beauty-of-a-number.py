class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        res = []
        for i in range(len(num)):
            for j in range(i+1, len(num)+1):
                res.append(num[i:j])
        total = 0
        for x in res:
            if int(x) ==0:continue
            if len(x) == k:
                if int(num)%int(x)==0: total += 1
        return total 