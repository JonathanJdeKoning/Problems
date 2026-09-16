from math import ceil, floor, inf
A, B, W = list(map(int, input().split()))

W *= 1000

mn =inf
mx = -1 
for i in range(0, W+1):
    if A*i <= W and W <= B*i:
        mn = min(mn, i)
        mx = max(mx, i)

if mx == -1:
    print("UNSATISFIABLE")
else:
    print(mn, mx)



