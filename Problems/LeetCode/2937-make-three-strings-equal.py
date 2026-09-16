class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if s1 == s2 == s3: return 0
        if not (s1[0]==s2[0]==s3[0]): return -1
        mn = min([len(s1),len(s2),len(s3)])
        
        total = 0
        total += len(s1) - mn
        total += len(s2) - mn
        total += len(s3) - mn
        total += mn*3
        for i in range(mn):
            if (s1[i]==s2[i]==s3[i]):
                total -= 3
            else:
                break
        return total
