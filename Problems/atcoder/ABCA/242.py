a,b,c,x = map(int, input().split())
if x <=a: print(1);exit()
if x > b: print(0); exit()
print(c*(1/(b-a)))
