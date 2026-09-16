x1, y1, x2, y2 = list(map(int, input().split()))

xDiff = x2 - x1
yDiff = y2 - y1

print(x2-yDiff, y2+xDiff,x1 - yDiff, y1 + xDiff)