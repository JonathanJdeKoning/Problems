class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xs = set()
        ys = set()
        for i in range(bound+1):
            v = x**i
            if v in xs:   break
            if v > bound: break
            xs.add(v)

        for i in range(bound+1):
            v = y**i
            if v in ys:   break
            if v > bound: break
            ys.add(v)
            
        ans = set()
        for a in xs:
            for b in ys:
                if a+b <= bound: ans.add(a+b)
        return list(ans)
        