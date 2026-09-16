class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        ans = 0
        curr = 0
        for rung in rungs:
            if rung - curr > dist:
                ans += (rung-curr)//dist
                if (rung-curr)%dist==0: ans -= 1
            curr = rung

        return ans