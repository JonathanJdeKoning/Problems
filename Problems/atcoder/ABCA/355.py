x,y = map(int,input().split())
if x==y: print(-1)
else:
    print(list(filter(lambda z: z != x and z != y, [1,2,3]))[0])
