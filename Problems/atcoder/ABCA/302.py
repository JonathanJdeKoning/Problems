a,b = map(int, input().split())
reps, left = divmod(a,b)
if left==0:print(reps)
else:print(reps+1)
