x,y = map(int, input().split())

g = {1:1,2:2,3:1,4:4,5:1,6:4,7:1,8:1,9:4,10:1,11:4,12:1}
if g[x] == g[y]:
    print("Yes")
else:
    print("No")
