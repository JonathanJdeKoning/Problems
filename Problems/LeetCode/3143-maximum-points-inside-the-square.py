class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        d = defaultdict(list)
        maxRange = inf
        for i, point in enumerate(points):
            tag = s[i]
            width = max(abs(point[0]), abs(point[1]))
            d[tag].append(width)
        
        new = defaultdict(int)
        for tag, dists in d.items():
            ala = sorted(dists)
            ala.append(99999999999)
            maxRange = min(maxRange, ala[1])
            new[tag] = ala[0]
            
        return len([x for x in new.values() if x < maxRange])
            
            
                
                
            