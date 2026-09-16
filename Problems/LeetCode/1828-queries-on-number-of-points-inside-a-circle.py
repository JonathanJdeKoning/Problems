class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for cx,cy,r in queries:
            res = 0
            for px,py in points:
                if dist((px,py), (cx,cy)) <= r:
                    res += 1
            ans.append(res)
        return ans
