from heapq import heappush, heappop
N = int(input())
h = []
X = []
Y = []
Z = []
A = [] 
L = [[None,None,None] for _ in range(N)]
seen = set()
ans = 0
for i in range(N):
    x,y,z = list(map(int, input().split()))
    A.append((x,y,z))
    X.append((x,i))
    Y.append((y,i))
    Z.append((z,i))
X.sort()
Y.sort()
Z.sort()
for i, (x,y,z) in enumerate(zip(X,Y,Z)):
    L[x[1]][0] = i
    L[y[1]][1] = i
    L[z[1]][2] = i

def getValidEdges(i):
    xIndex, yIndex, zIndex = L[i]
    xNum = X[xIndex][0]
    yNum = Y[yIndex][0]
    zNum = Z[zIndex][0]
    edges = []
    if xIndex > 0:
        xLeftNum, xLeftID = X[xIndex-1]
        if xLeftID not in seen:
            edges.append((abs(xLeftNum - xNum), xLeftID))
    if xIndex < len(X)-1:
        xRightNum, xRightID = X[xIndex+1]
        if xRightID not in seen:
            edges.append((abs(xRightNum - xNum), xRightID))
    if yIndex > 0:
        yLeftNum, yLeftID = Y[yIndex-1]
        if yLeftID not in seen:
            edges.append((abs(yLeftNum - yNum), yLeftID))
    if yIndex < len(Y)-1:
        yRightNum, yRightID = Y[yIndex+1]
        if yRightID not in seen:
            edges.append((abs(yRightNum - yNum), yRightID))
    if zIndex > 0:
        zLeftNum, zLeftID = Z[zIndex-1]
        if zLeftID not in seen:
            edges.append((abs(zLeftNum - zNum), zLeftID))
    if zIndex < len(Z)-1:
        zRightNum, zRightID = Z[zIndex+1]
        if zRightID not in seen:
            edges.append((abs(zRightNum - zNum), zRightID))
    return edges
seen.add(0)
for edge in getValidEdges(0):
    heappush(h, edge)

while h:
    dist, ID = heappop(h)
    if ID in seen: continue
    ans += dist
    seen.add(ID)
    for edge in getValidEdges(ID):
        heappush(h,edge)
print(ans)
