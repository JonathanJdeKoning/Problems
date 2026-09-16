from math import inf
N = int(input())
mn = inf


for _ in range(N):
    time, price, stock = list(map(int, input().split()))
    
    if stock - time > 0:
        mn = min(mn, price)
print(mn) if mn != inf else print(-1)