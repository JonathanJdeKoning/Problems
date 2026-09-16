class Solution:
    def minOperations(self, s: str) -> int:
        oddpos = 0
        evepos = 0
        for i,c in enumerate(s):
            if i%2==0:
                if c=="1":
                    evepos += 1
                    continue
                else:
                    oddpos +=1
                    continue
            
            if i%2==1:
                if c=="1":
                    oddpos += 1
                    continue
                else:
                    evepos += 1
                    continue
        return len(s) - max(oddpos, evepos)