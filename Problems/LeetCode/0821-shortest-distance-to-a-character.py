class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        out = [None]*len(s)
        dist = math.inf
        for i, p in enumerate(s):
            if p == c:
                dist = 0
            out[i] = dist
            dist += 1
        dist = math.inf
        for i, p in enumerate(s[::-1]):
            if p == c:
                dist = 0
            out[-(i+1)] = min(dist,out[-(i+1)])
            dist += 1
        return out
        
