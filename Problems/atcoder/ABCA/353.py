n = int(input())
h = list(map(int, input().split()))

s = h[0]

for i, b in enumerate(h[1:], start=2):
    if b > s: print(i);exit(0)
print(-1)
