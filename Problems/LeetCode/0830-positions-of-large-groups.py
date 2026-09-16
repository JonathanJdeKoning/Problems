class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        out = []
        run = 1
        start = 0
        curr = s[0]
        for i, c in enumerate(s[1:],start=1):
            if c == curr:
                run += 1
            else:
                if run >=3:
                    out.append([start,i-1])
                start = i
                run = 1
                curr = s[i]
        if run >=3:
            out.append([start,i])
        return out 
                
