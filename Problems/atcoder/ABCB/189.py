N, X = list(map(int, input().split()))

total = 0

for i in range(N):
    v, p = list(map(int, input().split()))
    
    total += v * p
    if total > X*100:
        exit(print(i+1))
print(-1) 