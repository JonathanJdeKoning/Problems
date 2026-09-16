class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        mx = 0
        for i,a in enumerate(points):
            for j, b in enumerate(points):
                for k, c in enumerate(points):
                    if j<= i or k <= j or k<= i: continue
                    x1,y1 = a
                    x2,y2 = b
                    x3,y3 = c


                    area = 0.5*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
                    mx = max(mx, area)
        return mx

