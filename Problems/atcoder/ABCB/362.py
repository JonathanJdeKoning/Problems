from math import dist, isclose
xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

ls = [dist((xa,ya),(xb,yb)),dist((xb,yb),(xc,yc)),dist((xc,yc),(xa,ya))]
ls.sort()

if isclose(ls[0]**2+ls[1]**2, ls[2]**2):
    print("Yes")
else:
    print("No")
