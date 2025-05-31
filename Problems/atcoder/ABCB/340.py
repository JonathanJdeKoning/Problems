q,a=int(input()),[]
for _ in range(q):
 o,v=input().split()
 if o=="1":a.append(v)
 else:print(a[-int(v)])
