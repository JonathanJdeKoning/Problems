x, y, X, Y = list(map(int, input().split()))


Y = -Y

slope = (Y - y) / (X - x)
c = y - slope * x

xIntercept = (-c) / slope
print(xIntercept)