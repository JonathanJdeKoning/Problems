class Solution:
    def minimumDeletions(self, s: str) -> int:
        bCount = [0]*len(s)
        best = inf
        a =0 
        b = 0

        for i,c in enumerate(s):
            bCount[i] = b

            if c =="b":
                b += 1

        for i,c in enumerate(s[::-1], start = 1):
            best = min(best, (a+bCount[-i]))
            if c == "a":
                a += 1

            
        return best

