class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        out = []
        balls = defaultdict(int)
        colors = defaultdict(int)
        curr = 0
        for ball, color in queries:
            prevColor = balls[ball]
            if color == prevColor:
                out.append(curr)
                continue
            
            balls[ball] = color
            
            currCount = colors[color]
            prevCount = colors[prevColor]
            
            colors[color] += 1
            colors[prevColor] -= 1
            
            if currCount == 0:
                curr += 1
            if prevCount == 1:
                curr-= 1
            out.append(curr)
        return out
            
            
            
            
            
        