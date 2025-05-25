a = list(map(int, input().split()))
redo =  sorted([x for x in a if x%25==0 and 100<=x<=675])
if a == redo: print("Yes")
else: print("No")
