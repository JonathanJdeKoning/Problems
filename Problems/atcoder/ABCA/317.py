n,h,x = map(int, input().split())
p = list(map(int, input().split()))

for i,z in enumerate(p):
    if z+h >= x: print(i+1);break
