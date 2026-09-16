class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)):
            dists = Counter()
            for j in range(len(points)):
                if j == i: continue
                dists[dist(points[i], points[j])] += 1
            for k, v in dists.items():
                ans += v*(v-1)
        return ans