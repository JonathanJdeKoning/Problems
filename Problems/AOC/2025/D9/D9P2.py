from shapely.geometry import Point, box
from shapely.geometry.polygon import Polygon

ans = 0
A = []
with open("data.in","r") as file:
    for line in file.readlines():
        x, y= map(int, line.strip().split(","))
        A.append((x,y))

poly = Polygon(A)
for i in range(len(A)-1):
    ax, ay = A[i]
    for j in range(i+1, len(A)):
        bx, by = A[j]
        rect = box(min(ax,bx), min(ay, by), max(ax,bx), max(by,ay)).buffer(-0.001)
        if poly.contains(rect):
            area = (1+abs(ax-bx)) * (1+abs(ay-by))
            ans = max(ans, area)
        
print(ans)