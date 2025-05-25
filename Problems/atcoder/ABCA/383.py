N = int(input())
A = []
for _ in range(N):
    t,v = list(map(int, input().replace(","," ").split()))
    A.append((t, v))

curr = 0
level = 0
for t in range(101):
    currT = A[curr][0]
    if currT == t:
        level += A[curr][1]
        curr += 1
        if curr == len(A): break
    level = max(0, level - 1)
print(level)
