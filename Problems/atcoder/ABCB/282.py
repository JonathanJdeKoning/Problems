N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(input())

ans = 0
for i in range(len(A)-1):
    for j in range(i+1, len(A)):
        for x, y in zip(A[i], A[j]):
            if x == "x" and y == "x":
                break
        else:
            ans += 1
print(ans)
                
