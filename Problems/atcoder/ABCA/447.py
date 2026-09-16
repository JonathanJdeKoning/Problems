N, M = map(int, input().split())

seated = 0
for i in range(1, N+1, 2):
    seated += 1
if seated >= M:
    print("Yes")
else:
    print("No")
