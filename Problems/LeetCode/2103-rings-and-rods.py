class Solution:
    def countPoints(self, rings: str) -> int:
        rods = defaultdict(set)
        for i in range(0,len(rings),2):
            data = rings[i:i+2]
            rods[data[1]].add(data[0])
        return len([k for k,v in rods.items() if len(v) == 3])