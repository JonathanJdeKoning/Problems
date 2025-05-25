x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())


xs = [x1,x2,x3]
ys = [y1,y2,y3]
xs = sorted(xs,key=lambda x:xs.count(x))
ys = sorted(ys,key=lambda y:ys.count(y))

print(xs[0], ys[0])
