class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        cx, cy = center
        ans = [[-1,-1,-1]]
        for x,y,q in towers:
            dist = abs(cx-x) + abs(cy-y)
            if dist > radius: continue

            ans.append([x,y,q])

        ans.sort(key = lambda x:(x[-1], -x[0], -x[1]))
        return ans[-1][:-1]