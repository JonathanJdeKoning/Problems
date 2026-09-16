class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        sectors = defaultdict(int)
        start=rounds[0]
        sectors[start]+=1
        for end in rounds[1:]:
            while True:
                start +=1
                if start%n==0:
                    sector = n
                else:
                    sector = start%n
                sectors[sector] += 1
                if sector == end:
                    start = sector
                    break
        mx = max(sectors.values())
        out = []
        for k,v in sectors.items():
            if v == mx:
                out.append(k)
        return sorted(out)



            


