class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        playas = defaultdict(int)
        for match in matches:
            a, b = match[0], match[1]
            playas[b] += 1
            playas[a] += 1
            playas[a] -= 1
        
        
        
        nevers = []
        oners = []
        for key, val in playas.items():
            if val == 1:
                oners.append(key)
            elif val == 0:
                nevers.append(key)
        return [sorted(nevers), sorted(oners)]

            
